import pandas as pd
import random

class Playlist():

    def __init__(self, filename):

        self.filename = filename
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
        return self.__df["Track ID"].dropna()
    
    @property
    def tracks(self):
        return self.__df["Track Name"].dropna()
    
    @property
    def albums(self):
        return self.__df["Album Name"].dropna()
    
    @property
    def artists(self):
        return self.__df["Artist Name(s)"].dropna()
    
    @property
    def releases(self):
        return self.__df["Release Date"].dropna()
    
    @property
    def durations(self):
        return self.__df["Duration (ms)"].dropna()
    
    @property
    def genres(self):
        return self.__df["Genres"].dropna()
    
    @property
    def labels(self):
        return self.__df["Record Label"].dropna()
    
    @property
    def tempos(self):
        return self.__df["Tempo"]
    
    def getSong(self, index):
        return self.__df.iloc[index]
    
    def getSongId(self, id):
        if id in self.__df["Track ID"].values:
            return self.__df[self.__df["Track ID"] == id].iloc[0]
    
    def randSong(self):
        rand = random.randint(0, self.length)
        return self.getSong(rand)
    
class Song():

    def __init__(self, pl, id = None):
        if isinstance(id, int):
            self.__song = pl.getSong(id)
        elif isinstance(id, str):
            self.__song = pl.getSongId(id)
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
        return self.__song["Duration (ms)"]
    
    @property
    def genre(self):
        return self.__song["Genres"]
    
    @property
    def label(self):
        return self.__song["Record Label"]
    
    @property
    def tempo(self):
        return self.__song["Tempo"]