from unittest import TestCase

from notes_cli import notes

class TestNotes(TestCase):
    def test_is_string(self):
        self.assertTrue(isinstance(notes.NOTES_PATH, str))
