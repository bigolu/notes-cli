"""
Command and all sub-commands of the notes cli
"""
import operator
import json
from pathlib import Path
from functools import reduce
import click
from fuzzywuzzy import fuzz

NOTES_PATH = '%s/.notes.json' %(Path('~').expanduser())
NOTES_FILE = Path(NOTES_PATH)

@click.group()
def notes():
    """A CLI for your notes"""
    pass

@notes.command()
def add():
    """ add new note"""

    assert NOTES_FILE.exists(), 'Notes not found, try running \'notes init\''

    note_name = click.prompt('Enter the note name')
    note_value = click.prompt('Enter the note')

    # load notes from local and add new note
    click.echo('Storing new note ...')

    all_notes = {}
    with NOTES_FILE.open('r') as notes_file:
        all_notes = json.load(notes_file)
        all_notes[note_name] = note_value

    with NOTES_FILE.open('w') as notes_file:
        json.dump(all_notes, notes_file)

    click.echo('Done!')

@notes.command()
def find():
    """ Search notes"""

    assert NOTES_FILE.exists(), 'Notes not found, try running \'notes init\''

    query = click.prompt('Enter query')

    with NOTES_FILE.open('r') as notes_file:
        all_notes = json.load(notes_file)
        # map notes keys to tuples in the form (key, similarity_ratio)
        possible_matches = [(x, fuzz.partial_ratio(x, query)) for x in all_notes.keys()]
        # retain only the keys which match well with the query
        matches = [x for x in possible_matches if x[1] > 50]

        # check for matches
        if not matches:
            click.echo('\nno matches found\n')
            return

        # sort by similarity
        matches.sort(key=operator.itemgetter(1))
        """ map matches to string in form 'note_name - note' 
        e.g. (note_name, value) ==> 1. note_name - value """
        matches = ['\n%d. %s - %s\n' %(num, x[0], all_notes[x[0]])
                   for num, x in enumerate(matches, 1)]
        # format and output results
        results = reduce(lambda x,y: '{}{}'.format(x, y), matches)
        click.echo(results)

@notes.command()
def init():
    """ Create file to store notes """

    should_make_notes = (not NOTES_FILE.exists()) or click.confirm('notes already found, overwrite?')

    if should_make_notes:
        with NOTES_FILE.open('w+') as notes_file:
            json.dump({}, notes_file)
            click.echo('notes files created!')
    else:
        click.echo('ok, aborting')
