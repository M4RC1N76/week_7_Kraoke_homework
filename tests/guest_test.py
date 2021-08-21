import unittest

# from src.room import Room
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Thomas")
        # self.song = Song("Aces High", "Iron Maiden", "Heavy Metal")

    def test_guest_has_name(self):
        self.assertEqual("Thomas", self.guest.name)


