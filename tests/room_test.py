import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Music") # checked correct
        self.room_2 = Room("Indie Rock")
        self.room_3 = Room("Reggae Songs")
        # rooms = [self.room_1, self.room_2, self.room_3]
        self.song_1 = Song("Helicopter", "Bloc Party", "Indie")
        self.song_2 = Song("Books from boxes", "Maximo Park", "Indie")
        self.song_3 = Song("Three Little Birds", "Bob Marley", "Reggae")
        # songs = [self.song_1, self.song_2, self.song_3]
        self.guest_1 = Guest("Thomas")
        self.guest_2 = Guest("Kevin")
        self.guest_3 = Guest("Lana")
        self.guest_4 = Guest("Dahlia")

    def test_room_has_name(self):
        self.assertEqual("Music", self.room_1.name)

    # room can add new song
    def test_room_can_add_song(self):
        self.room_3.add_song(self.song_3)
        self.assertEqual(self.room_3.song_queue[0], self.song_3) 
        # comparing room_3 song_queue List with added self.song_3

    # can add guest to room
    def test_empty_room_add_guest(self):
        self.room_2.check_in(self.guest_1)
        self.assertEqual(self.room_2.guest_queue[0], self.guest_1)

    # can remove guest
    def test_check_out(self):
        self.room_3.check_in(self.guest_4)
        self.room_3.check_out(self.guest_4)
        self.assertEqual([], self.room_3.guest_queue)
        # first check in guest than remove it
        # then compare empty list with empty guest queue