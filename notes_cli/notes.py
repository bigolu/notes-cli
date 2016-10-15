"""
Command and all sub-commands of the notes cli
"""
import operator
import json
import os
import click
from fuzzywuzzy import fuzz
from util.util import is_windows_machine
from git import Repo

NOTES_PATH = '%s/notes.json' %(os.path.dirname(os.path.abspath(__file__)))


@click.group()
def notes():
    """ Define the root command for cli"""
    pass

@notes.command()
def add():
    """ add new note"""

    # get the note
    note_name = click.prompt('Enter the note name')
    note_value = click.prompt('Enter the note')

    # load notes from local and and add new note
    click.echo('Storing new note ...')
    all_notes = {}
    with open(NOTES_PATH, 'r') as notes_file:
        all_notes = json.load(notes_file)
        all_notes[note_name] = note_value

    # write updated notes to json
    with open(NOTES_PATH, 'w') as notes_file:
        json.dump(all_notes, notes_file)
    click.echo('Done!')
    return

@notes.command()
def find():
    """ Search notes"""

    query = click.prompt('Enter query')
    with open(NOTES_PATH, 'r') as notes_file:
        all_notes = json.load(notes_file)
        # map notes keys to tuples in the form (key, similarity_ratio)
        possible_matches = [(x, fuzz.partial_ratio(x, query)) for x in all_notes.keys()]
        # retain only the keys which match well with the query
        matches = [x for x in possible_matches if x[1] > 50]
        # sort the matches by similarity
        matches.sort(key=operator.itemgetter(1))
        # map matches to string in form 'note_name - note'
        matches = ['\n%d. %s - %s\n' %(num, x[0], all_notes[x[0]])
                   for num, x in list(enumerate(matches, 1))]
        # format the output
        results = '\n\n'.join(matches)
        # output answers
        click.echo(results)
    return

if __name__ == '__main__':
    notes()
