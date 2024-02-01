class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    def add_song_to_count(self):
        Song.count += 1
        print("Curr Val of Song.count:" , Song.count)
       
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self , new_genre):
        if type(new_genre) is str:
            self._genre = new_genre
        else:
            raise Exception("You must use type string for the new genre.")
    
    def add_to_genres(new_genre):
        if new_genre not in Song.genres or len(Song.genres) <= 1:
            Song.genres.append(new_genre)
        else:
            None
    
    def add_to_genre_count(genre):
      if genre not in Song.genre_count.keys():
          Song.genre_count[genre] = 1
      else:
          Song.genre_count[genre] += 1




    @property
    def artist(self):
        return self._artist
    
    @artist.setter
    def artist(self, new_artist):
        if type(new_artist) is str:
            self._artist = new_artist
        else:
            raise Exception("Your artist name but be a string")
    
    def add_to_artists(new_artist):
        if new_artist not in Song.artists:
            Song.artists.append(new_artist)
        else:
            None

    def add_to_artist_count(new_artist):
        if new_artist not in Song.artist_count.keys():
            Song.artist_count[new_artist] = 1
        else:
            Song.artist_count[new_artist] += 1


# first = Song("Name of Song", "Joe", "Hip-Hop")
# second = Song("Name of Song 2", "Lisa", "Rap")
# third = Song("Name of Song 3", "ME", "Folk")
# fourth = Song("Name of Song 4", "ME", "Folk")
# print(first.name)
# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)