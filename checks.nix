{
  pkgs,
  stdenv,
  python3Packages,
  merise_dot ? pkgs.callPackage ./default.nix { },
  ...
}:

let
  reports = stdenv.mkDerivation {
    name = "merise_dot-behave-checks";

    # build info
    src = ./.;
    nativeBuildInputs =
      with pkgs;
      with python3Packages;
      [
        behave
        coverage
        merise_dot
        # build deps
        click
        questionary
        graphviz
      ];

    # actual build
    buildPhase = ''
      coverage run --source="./merise_dot" -m behave --junit -t "not @wip" || true
    '';

    # everything to reports
    installPhase = ''
      mkdir -p $out
      coverage xml -o $out/coverage
      coverage report > $out/coverage.txt
      cp -r reports $out/
    '';
  };
in
stdenv.mkDerivation {
  name = "merise_dot-behave-res";
  src = reports.out;
  dontInstall = true; # these are test reports, not a binary

  # build reports
  buildPhase = ''
    if grep 'status="failed"' reports/*
    then
      exit 1
    else
      touch $out
    fi
  '';

  # small passthru utility to ensure we get access to reports
  passthru = { inherit reports; };
}
