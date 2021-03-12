# cutefetch

cutefetch is a cute and minimal system information tool written in bash. Similarly to other fetch tools, it will fetch some information about your system and display it in a visually pleasing way beside an animal.

<p align="center"><img src="./previews/fetch.png" width="100%" height="auto"/></p>

## Install

cutefetch is just a bash script. To install it, just download the file (eg: `wget https://github.com/rayes0/scripts/raw/main/cutefetch/cutefetch`) and put it somewhere in your `$PATH`.

## Usage

```
Usage:
 cutefetch [ANIMAL]

Defaults to bunny if no animal specified.

Avaliable animals:
 bunny
 kitten
 puppy
 owl
 fish
 pika
 random (uses a random animal from the above list)
 none (no animal, only displays system info)

Options:
 -h, --help, help          Print this message
 -c, --config, config      Print configuration options
```

## Configuration

The default behaviour of cutefetch can be configured with environment variables. You may declare these either in a file run by bash on startup (eg: `~/.bashrc`), or manually using `export VARIABLE=VALUE`.

### Variables

```sh
# Sets the animal displayed by default if none are specified (default: bunny). For a list of animals, see `cutefetch -h`
CF_DEFAULT_ANIMAL=bunny

# Renders output with only the fg and bg colors (default: false)
# Valid: true|false
CF_MONOCHROME=false

# Whether or not to use bold for label text (default: true)
# Valid: true|false
CF_BOLD=true

# Whether or not to use italic for info text (default: false)
CF_ITALIC=(true|false)

# Whether or not to use italic for label text (default: false)
CF_ITALIC_LABELS=(true|false)

# Whether or not to display a title line containing the name of the current user and hostname (default:true)
# Valid: true|false
CF_TITLE=true

# Settings regarding whether labels are displayed in uppercase, lowercase, or titlecase (default:upper)
# Valid: upper|lower|title
CF_LABELS=upper
```

## Inspiration

- ![elenapan's bunnyfetch](https://github.com/elenapan/dotfiles/blob/master/bin/bunnyfetch)
- ![Luvella's bunnyfetch](https://github.com/Luvella/Bunnyfetch)
- ![neofetch](https://github.com/dylanaraps/neofetch) by dylanraps
