{ pkgs, stdenv, python3Packages,
merise_dot ? pkgs.callPackage ./default.nix { },... }:

let
  reports = stdenv.mkDerivation {
    name = "merise-dot-behave-checks";

    # build info
    src = ./.;
    nativeBuildInputs = with pkgs; with python3Packages; [
      behave
      coverage
      merise_dot
    ];

    # actual build
    # TODO
  };
in stdenv.mkDerivation {}
