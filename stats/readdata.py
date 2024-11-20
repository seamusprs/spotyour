import pandas as pd
import random

class Playlist():

    def __init__(self, filename):
        self.__df = pd.read_csv(filename + ".csv")

    def showtable(self):
        print(self.__df)

    @property
    def table(self):
        return (self.__df)

    @property
    def length(self):
        return len(self.__df)
    
    @property
    def ids(self):
        return self.__df["Track ID"]
    
    @property
    def tracks(self):
        return self.__df["Track Name"]
    
    @property
    def albums(self):
        return self.__df["Album Name"]
    
    @property
    def artists(self):
        return self.__df["Artist Name(s)"]
    
    @property
    def releases(self):
        return self.__df["Release Date"]
    
    @property
    def durations(self):
        return self.__df["Duration"]
    
    @property
    def genres(self):
        return self.__df["Genres"]
    
    @property
    def labels(self):
        return self.__df["Record Label"]
    
    @property
    def tempos(self):
        return self.__df["Tempo"]
    
    def getSong(self, index):
        return self.__df.iloc[index]
    
    def randSong(self):
        rand = random.randint(0, self.length)
        return self.getSong(rand)
    
class Song():

    def __init__(self, pl, index = None):
        if isinstance(index, int):
            self.__song = pl.getSong(index)
        else:
            self.__song = pl.randSong()

    @property
    def id(self):
        return self.__song["Track ID"]
    
    @property
    def track(self):
        return self.__song["Track Name"]
    
    @property
    def album(self):
        return self.__song["Album Name"]
    
    @property
    def artist(self):
        return self.__song["Artist Name(s)"]
    
    @property
    def release(self):
        return self.__song["Release Date"]
    
    @property
    def duration(self):
        return self.__song["Duration"]
    
    @property
    def genre(self):
        return self.__song["Genres"]
    
    @property
    def label(self):
        return self.__song["Record Label"]
    
    @property
    def tempo(self):
        return self.__song["Tempo"]