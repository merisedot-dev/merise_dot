# Getting started

In this section, we'll assume you're working using a `pyproject.toml` file for build purposes (`requirements.txt` still exists but we won't cover it).

## Adding `merise_dot` to your project

To add the library to your project, please add the following to your `pyproject.toml` :

```toml
dependencies = [ "merise_dot" ]
```

If you're using devshells, please refer to one of the following sections for the following devshell tool you're using.

### Nix

Add the following to your `flake.nix` :

```nix
inputs.merise_dot.url = "github:merisedot-dev/merise_dot";

outputs = {
    devShells.default = pkgs.mkShell {
        name = "myshell";
        packages = [ merise_dot ];
    };
};
```

## Simple graph


