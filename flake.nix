{
  description = "Merisedot main toolchain";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
  flake-utils.lib.eachDefaultSystem (system:
  let
    pkgs = import nixpkgs { inherit system; };
  in {
    # default build
    packages.default = pkgs.callPackage ./default.nix { };
    checks.default = pkgs.callPackage ./checks.nix { };

    # devShells for people who are lazy with env setup
    devShells.default = pkgs.mkShell {
      name = "merise_dot";
      inputsFrom = [ self.packages.${system}.default ];
      packages = with pkgs.python3Packages; with pkgs; [
        venvShellHook
        bumpver
        yapf
        just # some commands utility
        # test deps
        behave
        # python deps
        click
        questionary
        graphviz
      ];
      postVenvCreation = ''
        pip install -e .
      '';
      venvDir = ".venv";
      src = null;
    };
  });
}
