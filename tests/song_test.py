import unittest

from src.song import Song
from src.room import Room

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Helicopter", "Bloc Party", "Indie")

    def test_song_has_a_title(self):
        self.assertEqual("Helicopter", self.song.title)

    def test_song_has_an_artist(self):
        self.assertEqual("Bloc Party", self.song.artist)

    def test_song_has_a_genre(self):
        self.assertEqual("Indie", self.song.genre)
