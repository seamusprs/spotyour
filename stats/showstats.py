import pandas as pd
import stats.readdata as rd

def toMins(ms):
    totalsecs = ms // 1000
    mins = totalsecs // 60
    secs = totalsecs - mins * 60
    string = "%.0i min, %.0i sec" % (mins, secs)
    return string

class Playlist(rd.Playlist):

    @property
    def topLabel(self):
        topcounts = self.labels.value_counts()
        topvalue = topcounts.idxmax()
        topcount = topcounts.max()
        return [topvalue, topcount]
    
    @property
    def topArtists(self):
        topcounts = self.artists.value_counts()
        topvalue = topcounts.idxmax()
        topcount = topcounts.max()
        return [topvalue, topcount]
    
    @property
    def topGenres(self):
        genrelist = []
        for row in self.genres:
            for item in row.split(sep = ","):
                genrelist.append(item)
        genreseries = pd.Series(genrelist)
        topcounts = genreseries.value_counts()
        topvalue = topcounts.idxmax()
        topcount = topcounts.max()
        return [topvalue, topcount]
    
    @property
    def shortest(self):
        index = self.durations.idxmin()
        song = rd.Song(self, index)
        return [song.track, song.artist, toMins(song.duration)]
    
    @property
    def longest(self):
        index = self.durations.idxmax()
        song = rd.Song(self, index)
        return [song.track, song.artist, toMins(song.duration)]
    
    @property
    def slowest(self):
        index = self.tempos.idxmin()
        song = rd.Song(self, index)
        return [song.track, song.artist, str(int(song.tempo)) + " BPM"]
    
    @property
    def fastest(self):
        index = self.tempos.idxmax()
        song = rd.Song(self, index)
        return [song.track, song.artist, str(int(song.tempo)) + " BPM"]
    
    def plstats(self):
        print("Stats for playlist using %s.csv:" % (self.filename))
        print("------------------------------" + "-" * len(self.filename))
        print("This playlist has %i songs." % (self.length))
        if self.ids.is_unique:
            print("This playlist has no duplicate songs.")
        else: print("This playlist contains duplicate songs.")
        print("The shortest song is %s by %s with a duration of %s." % (self.shortest[0], self.shortest[1], self.shortest[2]))
        print("The longest song is %s by %s with a duration of %s." % (self.longest[0], self.longest[1], self.longest[2]))
        print("The slowest song is %s by %s with a tempo of %s." % (self.slowest[0], self.slowest[1], self.slowest[2]))
        print("The fastest song is %s by %s with a tempo of %s." % (self.fastest[0], self.fastest[1], self.fastest[2]))
        print("%s is the most represented artist with %s songs." % (self.topArtists[0], self.topArtists[1]))
        print("%s is the most represented genre with %s songs." % (self.topGenres[0].capitalize(), self.topGenres[1]))
        print("%s is the most represented record label with %s songs." % (self.topLabel[0], self.topLabel[1]))