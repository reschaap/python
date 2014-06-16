class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

hey_you = Song(["Hey you, out there all alone", 
                "Sitting naked by the phone",
                "Would you touch me?"])

hey_you.sing_me_a_song()

radiohead = ["In a fast german car", "I'm amazed that I survived",
             "An aibag saved my life"]

airbag = Song(radiohead)

airbag.sing_me_a_song()