# notes-cli

## Description
Sometimes when you're using the shell, you can forget certain commands that are annoying to Google or where you are storing something, etc... 
With this you can make notes of these things and then query your notes later if you forget.

## Installation
1. install [pip](https://pip.pypa.io/en/stable/installing/)
2. run `pip install notes-cli && notes init`
4. and you're done!

## Docs
* `notes init`: creates a new a file to store all your notes. Stores it as '.notes.json' in your home directory.
* `notes add`: Prompts your for the note name and note value. For example:
    * Enter note name: extract a tar file
    * Enter note value: tar -xvf <filename\>
* `notes find`: prompts you for your search query and returns the top results.

## Thanks
This [great guide](https://python-packaging.readthedocs.io/en/latest/) on creating python packages and cli's, [click](http://click.pocoo.org/5/) for creating the cli, and [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) for searching.