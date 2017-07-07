"""
Printing information from a tuple.
"""
album = "VAMPS", "Sex Blood and Rock n' Roll", 2013, "Rock", ((1, "Devil Side"), (2, "Redrum"), (3, "Revolution II"), (4, "The Past"), (5, "Love Addict"))
artist, title, year, genre, tracks = album
print("Artist: " + artist)
print("Album title: " + title)
print("Genre: " + genre)
for i in tracks:
    track, song = i
    print("Track {0}: {1}".format(track, song))
