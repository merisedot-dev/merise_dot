# Merise-dot

Small python utility intended for MERISE display and modelisation through a shell. No GUI will be provided here, but feel free to implement one for this tool if you feel like it.

## Installation

As of now, no pip release has been done, no more than a nixpkgs one. Since this is the first published build, please refer to one of the following options :

### Nix

If you're as well a [Nix] enjoyer (or you're lazy like me), please run one of the following commands to install this in your Nix profile (nix-env also works but isn't recommended as of now) :

```nix
nix profile install github.com:Khelda/merise-dot
nix-env -iA github.com:Khelda/merise-dot
```

### Pipx

For those who appreciate a more... Traditional approach of installation, please turn to `pip` and its twin brother, `pipx`. In case of a `pipx` installation, please run the following commands to install :

```shell
git clone https://github.com/Khelda/merise-dot/ --depth=1
cd merise-dot
pipx install -e .
```

## Usage

This software is made to be imported in any tool needing to manipulate *MCD* graphs, or anything merise-related. Please refer to the [features] descriptions to know how to use this library.

[Nix]: https://nixos.org/
[features]: ./features/
[Gherkin]: https://cucumber.io/
