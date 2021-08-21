class Room:
    def __init__(self, name):
        self.name = name
        self.song_queue = [] # list of songs for the class rooms
        self.guest_queue =[] # list of guests for the class rooms
        # self.till = till # extension
        # self.max_capacity = max_capacity # oextension or put an int here max 3 peopele

    def add_song(self, song):
        # add given song to song queue
        self.song_queue.append(song)

    def check_in(self, guest):
        self.guest_queue.append(guest)

    def check_out(self, guest):
        self.guest_queue.remove(guest)

