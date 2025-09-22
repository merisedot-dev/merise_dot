{ pkgs, stdenv, python3, python3Packages, fetchPypi, hatch, ... }:

let
  merisedot_version = "0.1.0";

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
in python3Packages.buildPythonApplication {
  pname = "merise_dot";
  version = merisedot_version;

  src = ./.;
  format = "pyproject";

  nativeBuildInputs = with python3Packages; [ hatch hatch-build-scripts ];
  buildInputs = with python3Packages; [ click rich ];
}
