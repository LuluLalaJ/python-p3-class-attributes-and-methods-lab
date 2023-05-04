class Song:
    artists = []
    genres = []
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        Song.count += 1
        self.artist = artist
        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
        elif artist in Song.artists:
            Song.artist_count[artist] += 1
        self.name = name
        self.genre = genre
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        elif genre in Song.genres:
            Song.genre_count[genre] += 1
