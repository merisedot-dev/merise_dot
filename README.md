# Merise-dot

Small python utility intended for MERISE display and modelisation through a shell. No GUI will be provided here, but feel free to implement one for this tool if you feel like it.

## Installation

As of now, no pip release has been done, no more than a nixpkgs one. Since this is the first published build, please refer to one of the following options :

### Nix

If you're as well a [Nix] enjoyer (or you're lazy like me), please run the following command to use the software and get access to its manual :

```shell
nix run github.com:Khelda/merise-dot -- --help
```

Since it may be called upon often, you would be well-advised to alias that in your shell configuration for ease of use. You can also run this if you like using `nix profile` more :

```nix
nix profile install github.com:Khelda/merise-dot
```

### Pipx

For those who appreciate a more... Traditional approach of installation, please turn to `pip` and its twin brother, `pipx`. In case of a `pipx` installation, please run the following commands to install :

```shell
git clone https://github.com/Khelda/merise-dot/ --depth=1
cd merise-dot
pipx install -e .
```

## Usage

Just run the script and refer to its manual. Once launched, you will be prompted with different actions you can take to edit your MCD graph. If you need more detailed use cases, the [features] directory has you covered.

[Nix]: https://nixos.org/
[features]: ./features/
[Gherkin]: https://cucumber.io/
