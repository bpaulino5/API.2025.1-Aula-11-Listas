#Beatriz Paulino
#EX06

playlist = ["Imagine",
            "Bohemian Rhapsody",
            "Yesterday",
            "Hey Jude",
            "Let It Be"]

print(f"Três primeiras músicas da playlist: {playlist[:3]}")


playlist1 = playlist.copy()
playlist1.sort()
print(f"Playlist em ordem alfabética: {playlist1}")

favoritas = [playlist[3:]]
print(f"Playlist com as músicas favoritas: {favoritas}")