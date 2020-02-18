deck = []
suits = ["♠","♣","♦","♥"]

for i in range(4):
    for j in range(1,14):
        value = str(j)
        if(j == 1):
            value = "A"
        elif(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        deck.append(f"{value}{suits[i]}")

print(deck)
### at this point, commit to github under Simulation

# shuffle the deck - lookup Fisher Yates Shuffle - implement it in Python w/ your deck

# print the shuffled deck
### at this point, commit a second time to github, same file...
# turn in ##two histories## on Google Classroom
