genre = input("What genre of game do you like? ") # samlar in input från användaren om vilken genre av spel de gillar
platform = input("What platform do you want to play on? ") #samlar in input från användaren om vilken plattform de vill spela på
age = input("What age limit do you want?") #samlar in input från användaren om vilken åldersgräns de vill ha
#databas med spel alternativ
games=[
        {"title": "Call of Duty: Modern Warfare", "genre": "First-person-shooter", "age": "18", "platform": "Xbox"},
        {"title": "The Last of Us Part II", "genre": "Action-adventure", "age": "18", "platform": "PlayStation"},
        {"title": "Among Us", "genre": "Party game", "age": "10", "platform": "mobile"},
        {"title": "Phasmophobia", "genre": "Psychological-horror", "age": "15", "platform": "Pc"},
        {"title": "Counter-strike", "genre": "First-person-shooter", "age": "18", "platform": "Pc"},
        {"title": "Minecraft", "genre": "Sandbox-survival", "age": "7", "platform": "Nintendo Switch"},
        {"title": "Gears of War", "genre": "Third-person-shooter", "age": "18", "platform": "Xbox"},
        {"title": "Zelda breath of the wild", "genre": "Action-adventure", "age": "12", "platform": "Nintendo Switch"},
        {"title": "Golf with friends", "genre": "casual-party", "age": "3", "platform": "Pc"},
        {"title": "civilization 6", "genre": "turn-based-strategy", "age": "12", "platform": "Pc"},
        {"title": "Apex Legends", "genre": "Battle-royale", "age": "16", "platform": "PlayStation"},
        {"title": "Marvel Rivals", "genre": "Hero-shooter", "age": "12", "platform": "Pc"},
        {"title": "Mario kart 8 deluxe", "genre": "Racing", "age": "3", "platform": "Nintendo Switch"},
    ]
#rekommendationer
recommendations = 0

i = 0  # index för att ha koll på antal spel som rekomenderas

satisfied = False  # ← fix 1: satisfied måste definieras innan den används


while True:  
    game = games[i]
    score = 0
    if game["age"] == age:    #om spelet har samma åldersgräns som användaren så får det 1 poäng
        score += 1
    if game["platform"] == platform: #om spelet har samma plattform som användaren så får det 1 poäng
        score += 1
    if genre in game["genre"]: #om spelet har samma genre som användaren så får det 2 poäng
        score += 2
    if score >= 2:
        print(game["title"]) #skriver ut om spelet hr fått 2 eller fler poäng
        recommendations += 1 #om spelet har fått 2 eller fler poäng så ökar rekomendationerna med 1
    i += 1 #ökar indexet med 1 så att loopen går vidare till nästa spel i listan
 
 #om det rekomenderas 4 spel så frågar den användaren om de är nöjda med rekomendationerna")
    if recommendations == 4:
        answer = input("Are you satisfied with the recommendations? (yes/no) ")
        if answer == "yes":
            satisfied = True
        else:              # ← fix 3: else på rätt indentering
            recommendations = 0
        i += 1             #ökar indexet med 1 så att loopen går vidare till nästa spel i listan
#om den inte hittar något att rekomenderar skriver den ut "Sorry, I couldn't find any games that match your preferences."
    if recommendations == 0:
        print("Sorry, I couldn't find any games that match your preferences.")
print("My recommendation for you is: " + str(recommendations) + " titles") #skriver ut hur många spel som rekomenderades till användaren