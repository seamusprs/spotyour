### Project idea: Personalized Spotify Playlist Stats & Quiz: Spot your Spotify.

A package that contains two subpackages: stats and quiz. Stats allows users to gain insights about their Spotify playlist such as top artist, longest song, slowest song, etc. Quiz allows users to enter a game where they will be questioned on how well they know their playlist. The program will read a CSV file of the user playlist that users can obtain using Exportify.

**Package**: spotyourspotify
  - **Subpackage**: stats

    - **Module**: readdata

      - **Functions**: readdata, maketable, showtable, cleandata? (could include a function to split multiple artists, genres)

    - **Module**: showstats

      - **Functions**: getoptions, toplabels, topartist, topgenres, longestsong, shortestsong, fastestsong, slowestsong, showallstats

  - **Subpackage**: quiz

    - **Module**: makequiz

      - **Functions**: makequestion, various functions for different question types:
        - What artist performs this song?
        - Which song is longest / shortest?
        - Which artist do you have the most / fewest songs?
        - Which song is the oldest / newest?
        - Which of these songs is written by an X artist?
        - Function to keep score throughout quiz

    - **Module**: playgame

      - **Functions**: getoptions, setseed, playgame, scoreboard?
