{ pkgs, stdenv, python3, python3Packages, fetchPypi, hatch, ... }:

let
  merisedot_version = "1.1.0";

  # build scripts
  hatch-build-scripts = python3Packages.buildPythonPackage rec {
    pname = "hatch-build-scripts";
    version = "0.0.4";
    format = "pyproject";

    buildInputs = [ hatch ];
    src = fetchPypi {
      inherit version;
      pname = "hatch_build_scripts";
      sha256 = "sha256-x4UgmGkH5HU48suyT95B7fwsxV9FK1Ni+64Vzk5jRPc=";
    };
  };

  # selector package
  pzpPkg = python3Packages.buildPythonPackage rec {
    pname = "pzp";
    version = "0.0.28";
    format = "pyproject";
    build-system = with python3Packages; [ setuptools ];

    src = fetchPypi {
      inherit version pname;
      sha256 = "sha256-xO3x2v5yT5cxz4pa7Ug/f2sQFkJcMIVSWLfj/Lm70E4=";
    };
  };
in python3Packages.buildPythonApplication {
  pname = "merise_dot";
  version = merisedot_version;

  src = ./.;
  format = "pyproject";

  nativeBuildInputs = with python3Packages; [ hatch hatch-build-scripts ];
  propagatedBuildInputs = with python3Packages; [
    click
    questionary
    graphviz
    pzpPkg
  ];
}
