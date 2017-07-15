# notes-cli

![alt tag](https://raw.githubusercontent.com/biggie96/notes-cli/master/README_ASSETS/tar.png)

When using the shell, it's easy to forget certain commands, but with this you can make notes of them and refer to it later if you forget.

## Installation
This package uses python3 so you will need pip3 to install it.

#### Ubuntu:
- `sudo apt-get install python3-setuptools && sudo easy_install3 pip`

#### macOS:
- `brew install python3`

Once you have it, run `pip3 install notes-cli` (run as admin/root if errors occur) and you're done!

## Docs
* `notes init`: creates a new a file to store all your notes. Stores it as '.notes.json' in your home directory.
* `notes add`: Prompts your for the note name and note value. For example:
    * Enter note name: extract a tar file
    * Enter note value: tar -xvf <filename\>
* `notes find`: prompts you for your search query and returns the top results.

## Thanks
This [great guide](https://python-packaging.readthedocs.io/en/latest/) on creating python packages and cli's, [click](http://click.pocoo.org/5/) for creating the cli, and [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) for searching.
