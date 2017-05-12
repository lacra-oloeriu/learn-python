class Song(object):

     def __init__(self, lyrics):
         self.lyrics = lyrics

     def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

little_fishies = Song(["Five little fishies , swimming to a pool",
                   "The first one said",
                   "The pool is cool"])

little_one_fingers =Song(["Wiggle five fingers",
                       "Show one fingers"])

little_fishies.sing_me_a_song()

little_one_fingers.sing_me_a_song()
