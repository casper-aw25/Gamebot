genre = input("What genre of game do you like? ").lower()  # ← Lägg till .lower()
platform = input("What platform do you want to play on? ").lower()  # Användaren ska kunna skriva i små bokstäver och det ska fortfarande fungera
age = input("What age limit do you want?")

games = [
    {"title": "Call of Duty: Modern Warfare", "genre": "Fps", "age": "18", "platform": "Xbox"},
    {"title": "The Last of Us Part II", "genre": "Action-adventure", "age": "18", "platform": "PlayStation"},
    {"title": "Among Us", "genre": "Party game", "age": "10", "platform": "mobile"},
    {"title": "Phasmophobia", "genre": "Psychological-horror", "age": "15", "platform": "Pc"},
    {"title": "Counter-strike", "genre": "fps", "age": "18", "platform": "Pc"},
    {"title": "Minecraft", "genre": "Sandbox-survival", "age": "7", "platform": "Nintendo Switch"},
    {"title": "Gears of War", "genre": "Third-person-shooter", "age": "18", "platform": "Xbox"},
    {"title": "Zelda breath of the wild", "genre": "Action-adventure", "age": "12", "platform": "Nintendo Switch"},
    {"title": "Golf with friends", "genre": "casual-party", "age": "3", "platform": "Pc"},
    {"title": "civilization 6", "genre": "turn-based-strategy", "age": "12", "platform": "Pc"},
    {"title": "Apex Legends", "genre": "Battle-royale", "age": "16", "platform": "PlayStation"},
    {"title": "Marvel Rivals", "genre": "Hero-shooter", "age": "12", "platform": "Pc"},
    {"title": "Mario kart 8 deluxe", "genre": "Racing", "age": "3", "platform": "Nintendo Switch"},
    {"title": "Playerunknown's battlegrounds", "genre": "Battle-royale", "age": "16", "platform": "Pc"},
    {"title": "Splatoon 3", "genre": "Third-person-shooter", "age": "12", "platform": "Nintendo Switch"},
    {"title": "Rainbow six siege", "genre": "Tactical-shooter", "age": "18", "platform": "PlayStation"},
    {"title": "Overwatch", "genre": "Hero-shooter", "age": "12", "platform": "Pc"},
    {"title": "GTA V", "genre": "Action-adventure", "age": "18", "platform": "PlayStation"},
    {"title": "Elden Ring", "genre": "Rpg", "age": "18", "platform": "Pc"},
    {"title": "Monster Hunter World", "genre": "Rpg", "age": "16", "platform": "Pc"},
    {"title": "Assassin's Creed Shadows", "genre": "Rpg", "age": "18", "platform": "Xbox"},
    {"title": "Hunt showdown 1896", "genre": "Battle-royale", "age": "18", "platform": "Pc"},
    {"title": "TABG", "genre": "Battle-royale", "age": "12", "platform": "Pc"},
    {"title": "super animal royale", "genre": "Battle-royale", "age": "12", "platform": "Nintendo Switch"},
    {"title": "Halo Infinite", "genre": "Fps", "age": "18", "platform": "Xbox"},
]

satisfied = False
shown_games = []

def find_games():
    global satisfied
    
    while not satisfied:
        recommendations = 0
        i = 0
        current_recommendations = [] 
        
        while i < len(games) and recommendations < 4:   #Max antal rekomendationer
            game = games[i]
            score = 0
            
            if game["age"] == age:
                score += 1
            if game["platform"].lower() == platform:  # ← Lägg till .lower()
                score += 1
            if genre in game["genre"].lower():  # ← Lägg till .lower()
                score += 2
            
            if score >= 2 and game["title"] not in shown_games:
                print(game["title"])
                recommendations += 1
                current_recommendations.append(game["title"])
            
            i += 1
        
        shown_games.extend(current_recommendations) #Om de finns fler än 4 rekomendationer lagrar den dem i en annan lista
        
        if recommendations == 0:
            print("Sorry, I couldn't find any more games that match your preferences.") #om man inte är nöjd, men rekomendationer inte finns
            satisfied = True
        else:
            print("My recommendation for you is: " + str(recommendations) + " titles")
            answer = input("Are you satisfied with the recommendations? (yes/no) ").lower()  
            if answer == "yes":
                satisfied = True
                print("Great! Enjoy your gaming!")

if __name__ == "__main__":
    find_games()