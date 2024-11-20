import pandas as pd
import readdata as rd

class Playlist(rd.Playlist):
    
    @property
    def topLabel(self):
        counts = {}
        for i in range(0, self.length):
            song = rd.Song(self, i)
            if song not in counts:
                counts[song.label] = 1
            else:
                counts[song.label] += 1
        
        toplabel = max(counts, key=counts.get)
        topcount = counts[toplabel]
        result = [toplabel, topcount]

        # toplabel = self.labels.mode()
        # topcounts = toplabel.count()

        # return [toplabel, topcounts]




testpl = Playlist("spotyour\playlist")
print(testpl.topLabel)