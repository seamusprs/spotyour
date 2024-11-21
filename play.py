import stats.readdata as rd
import stats.showstats as ss

print("Welcome to Spot Your Spotify!")
print("Please select a playlist.")

inp = ""

while inp != "exit":
    inp = input("Enter path to playlist csv without file extension: ").lower()
    if inp == "": pl = rd.Playlist("playlist")
    else:
        try:
            pl = rd.Playlist(inp)
        except:
            print("Invalid file path! Please try again, or leave blank to use example playlist")
            continue

    while inp != "exit":
        print("Please enter 'stats' for playlist information, 'quiz' for the quiz game, 'new' to change playlist, or 'exit' to exit.")
        if inp == "exit" or inp == "new": 
            break
        elif inp == "stats": 
            pl.plstats()
        elif inp == "quiz": 
            # run quiz here
            pass
        else:
            print("Input not accepted, please try again")
            continue

print("Goodbye!")