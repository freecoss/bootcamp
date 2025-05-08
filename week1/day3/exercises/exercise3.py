class Song():
    def __init__(self, lyrics:list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

creep= Song(["When you were here before","couldn't look you in the eye", "You're just like an angel","your skin makes me cry"])
creep.sing_me_a_song()