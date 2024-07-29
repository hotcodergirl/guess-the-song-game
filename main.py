import time

def loading():
    time.sleep(2)
    
    
    

print("\nThis is a 'Guess the Song' Game. It can be played by two players or two player teams.")
print("The game consists of a total of 10 rounds, 5 rounds for each player/team.")
print("In each round, a lyric consisting a few words will be displayed from a song of any genre.") 
print("Each player/team will play alternatingly - they will only get 3 tries in 1 round to guess it.")
print("If the they guess the song name correctly, they will earn 10 points.")
print("If not, the points will stay the same.")
print("After playing 5 rounds each, the player/team with the highest number of points will be the winner.\n")
print("NOTE: Player/team must type in following valid formats(all should be in Title case):\n")
print("1. Song Name")
print("2. Song Name by Artist (and Artist2 if applicable)")
print("3. Song Name by Artist ft Featuring Artist (if applicable)")
loading()
songs = {}

songs[1] = ["Sometimes all I think about is you\nLate nights in the middle of June", "Heat Waves by Glass Animals", "Heat Waves"]

songs[2] = ["Ladies and gentlemen, will you please stand? With every guitar string scar on my hand", "Lover by Taylor Swift", "Lover"]

songs[3] = ["I just landed in, Chase B mixes pop like Jamba Juice\nDifferent colored chains, think my jeweler really sellin' fruits", "Sicko Mode by Travis Scott ft. Drake", "Sicko Mode by Travis Scott", "Sicko Mode"]

songs[4] = ["Why you gotta be so rude? Don't you know I'm human too?", "Rude by Magic!", "Rude"]

songs[5] = ["When I'm away from you I miss your touch\nYou're the reason why I believe in love", "Stay by The Kid Laroi and Justin Bieber", "Stay"]

songs[6] = ["And I know she'll be the death of me\nAt least we'll both be numb\nAnd she'll always get the best of me\nThe worst is yet to come", "Can't Feel My Face by The Weeknd", "Can't Feel My Face"]

songs[7] = ["If you want my future, forget my past\nIf you wanna get with me, better make it fast\nNow don't go wasting my precious time\nGet your act together we could be just fine", "Wannabe by Spice Girls", "Wannabe"]

songs[8] = ["Your insecure, don't know what for\nYou're turning heads when you walk through the door\nDon't need make up, to cover up\nBeing the way that you are is enough", "What Makes You Beautiful by One Direction", "What Makes You Beautiful"]

songs[9] = ["Now he's thinking bout me every night, oh\nIs is that sweet? I guess so\nSay you can't sleep, baby, I know\nThat's that me, espresso", "Espresso by Sabrina Carpenter", "Espresso"]

songs[10] = ["Needless to say, I keep her in check\nShe was a bad-bad nevertheless", "Sunflower by Post Malone and Swae Lee", "Sunflower"]

points_player1 = 0
points_player2 = 0 

for i in range(1, 11, 2):
    print("\nPlayer 1")
    print("\n" + songs[i][0] + "\n")
    loading()
    for x in range(3):
        user_input = input("Guess the song: \n")
        if user_input in songs[i]:
            points_player1 += 10
            print(f"Yay!\nPlayer 1 points: {points_player1}\nPlayer 2 points: {points_player2}")
            break
    else:
        print(f"\nWrong answer loser. Song: {songs[i][1]}\n")
        print(f"Player 1 points: {points_player1}\nPlayer 2 points: {points_player2}")
    loading()
    print("\nPlayer 2")jb
    print("\n" + songs[i + 1][0] + "\n")
    loading()
    for x in range(3):
        user_input = input("Guess the song: \n")
        if user_input in songs[i + 1]:
            points_player2 += 10
            print(f"Yay!\nPlayer 1 points: {points_player1}\nPlayer 2 points: {points_player2}")
            break
    else:
        print(f"\nWrong answer loser. Song: {songs[i + 1][1]}\n")
        print(f"Player 1 points: {points_player1}\nPlayer 2 points: {points_player2}")

loading()

if points_player1 > points_player2:
    print("Player 1 is the Winner!!!")

elif points_player1 < points_player2:
    print("Player 2 is the Winner!!!")

elif points_player1 == points_player2 and points_player1 != 0:
    print("It's a tie!!!")

elif points_player1 == 0 and points_player2 == 0:
    print("You both suck, I'm gonna sponsor your spotify membership lol")
