### Project idea: Personalized Spotify Playlist Stats & Quiz: Spot your Spotify.

A package that contains two subpackages: stats and quiz. Stats allows users to gain insights about their Spotify playlist such as top artist, longest song, slowest song, etc. Quiz allows users to enter a game where they will be questioned on how well they know their playlist. The program will read a CSV file of the user playlist that users can obtain using Exportify.

**Package**: spotyourspotify
  - **Subpackage**: stats: contains all the code for parsing and analysing playlist

    - **Module**: readdata: for parsing the playlist

      - **Functions**: 
        - readdata: converting csv file input to dataframe
        - showtable: displays input dataframe (mainly for troubleshooting)
        - cleandata: fixes any potential issues with dataframe (NA values, bad values, etc)
        - properties: various functions that return information about the playlist/songs
        - getsong: functions to get song as an object by index, or by song id, or randomly, depending on context

    - **Module**: showstats: contains the code for analysing playlist and giving fun stats

      - **Functions**: 
        - toplabel/topartist/topgenre: returns most represented record label, artist, or genre in the playlist
        - longestsong/shortestsong: returns longest or shortest song based on duration column
        - fastestsong/slowestsong: returns fastest or shortest song based on tempo column
        - showallstats: returns a list of various stats

  - **Subpackage**: quiz

    - **Module**: makequiz

      - **Functions**: 
        - makequestion
        - various functions for different question types:
        - What artist performs this song?
        - Which song is longest / shortest?
        - Which artist do you have the most / fewest songs?
        - Which song is the oldest / newest?
        - Which of these songs is written by an X artist?
        - Function to keep score throughout quiz

    - **Module**: playgame

      - **Functions**: getoptions, setseed, playgame, scoreboard?
