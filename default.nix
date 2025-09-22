{ pkgs, stdenv, python3, python3Packages, ... }:

let
  merisedot_version = "0.1.0";
in python3Packages.buildPythonApplication {
  pname = "merise_dot";
  version = merisedot_version;

  src = ./.;
  format = "pyproject";

  nativeBuildInputs = with python3Packages; [ setuptools ];
  buildInputs = with python3Packages; [ click rich ];
}
