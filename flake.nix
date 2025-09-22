{
  description = "Merisedot main toolchain";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
  flake-utils.lib.eachDefaultSystem (system:
  let
    pkgs = import nixpkgs {inherit system; };
  in {
    packages.default = pkgs.callPackage ./default.nix { };
    devShells.default = pkgs.mkShell {
      name = "merise-dot";
      inputsFrom = [ self.packages.${system}.default ];
      buildInputs = with pkgs.python3Packages; with pkgs; [
        venvShellHook
        bumpver
        yapf
        # test deps
        behave
        # python deps
        rich
        click
      ];
      postVenvCreation = ''
        pip install -e .
      '';
      venvDir = ".venv";
      src = null;
    };
  });
}
