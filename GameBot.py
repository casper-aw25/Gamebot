genre = input("What genre of game do you like? ").lower() #gör användarens input till lowercase
platform = input("What platform do you want to play on? ").lower() 
age = input("What age limit do you want?") #tar in ålder som string för att matcha speldatata

games = [   #lista med spel, varje spel är en dictionary med titel, genre, åldersgräns och plattform
    # FPS
    {"title": "Call of Duty: Modern Warfare", "genre": "fps", "age": "18", "platform": "xbox"},
    {"title": "Counter-strike", "genre": "fps", "age": "18", "platform": "pc"},
    {"title": "Halo Infinite", "genre": "fps", "age": "18", "platform": "xbox"},
    {"title": "Titanfall 2", "genre": "fps", "age": "16", "platform": "pc"},
    {"title": "Doom Eternal", "genre": "fps", "age": "18", "platform": "playstation"},
    {"title": "Battlefield 2042", "genre": "fps", "age": "18", "platform": "xbox"},
    {"title": "Borderlands 3", "genre": "fps", "age": "18", "platform": "playstation"},
    {"title": "Quake Champions", "genre": "fps", "age": "16", "platform": "pc"},
    {"title": "Far Cry 6", "genre": "fps", "age": "18", "platform": "playstation"},
    {"title": "Bioshock Infinite", "genre": "fps", "age": "18", "platform": "pc"},
    {"title": "Escape from Tarkov", "genre": "fps", "age": "18", "platform": "pc"},
    {"title": "Crysis 3 Remastered", "genre": "fps", "age": "16", "platform": "playstation"},

    # Action-Adventure
    {"title": "The Last of Us Part II", "genre": "action-adventure", "age": "18", "platform": "playstation"},
    {"title": "Zelda breath of the wild", "genre": "action-adventure", "age": "12", "platform": "nintendo switch"},
    {"title": "GTA V", "genre": "action-adventure", "age": "18", "platform": "playstation"},
    {"title": "Red Dead Redemption 2", "genre": "action-adventure", "age": "18", "platform": "pc"},
    {"title": "Marvel's Spider-Man 2", "genre": "action-adventure", "age": "16", "platform": "playstation"},
    {"title": "Batman: Arkham Knight", "genre": "action-adventure", "age": "18", "platform": "pc"},
    {"title": "Ghost of Tsushima", "genre": "action-adventure", "age": "18", "platform": "playstation"},
    {"title": "Hollow Knight", "genre": "action-adventure", "age": "7", "platform": "nintendo switch"},
    {"title": "Uncharted 4", "genre": "action-adventure", "age": "16", "platform": "playstation"},
    {"title": "Cyberpunk 2077: Phantom Liberty", "genre": "action-adventure", "age": "18", "platform": "pc"},
    {"title": "Horizon Zero Dawn", "genre": "action-adventure", "age": "12", "platform": "playstation"},
    {"title": "Devil May Cry 5", "genre": "action-adventure", "age": "18", "platform": "xbox"},
    {"title": "Prince of Persia: The Lost Crown", "genre": "action-adventure", "age": "12", "platform": "nintendo switch"},
    
    # Party & Casual
    {"title": "Among Us", "genre": "party game", "age": "10", "platform": "mobile"},
    {"title": "Golf with friends", "genre": "casual-party", "age": "3", "platform": "pc"},
    {"title": "Mario kart 8 deluxe", "genre": "racing", "age": "3", "platform": "nintendo switch"},
    {"title": "Fall Guys", "genre": "party game", "age": "7", "platform": "pc"},
    {"title": "Overcooked 2", "genre": "casual-party", "age": "3", "platform": "nintendo switch"},
    {"title": "Jackbox Party Pack 10", "genre": "party game", "age": "12", "platform": "playstation"},
    {"title": "Rocket League", "genre": "casual-party", "age": "3", "platform": "pc"},
    {"title": "Pummel Party", "genre": "party game", "age": "10", "platform": "pc"},
    {"title": "Super Smash Bros. Ultimate", "genre": "party game", "age": "7", "platform": "nintendo switch"},
    {"title": "Minecraft Party", "genre": "casual-party", "age": "7", "platform": "xbox"},
    {"title": "EA Sports FC 25", "genre": "casual-party", "age": "3", "platform": "playstation"},
    {"title": "Worms Armageddon", "genre": "party game", "age": "7", "platform": "pc"},
    {"title": "Stick Fight: The Game", "genre": "party game", "age": "7", "platform": "pc"},
    
    # Horror & Strategy
    {"title": "Phasmophobia", "genre": "psychological-horror", "age": "15", "platform": "pc"},
    {"title": "civilization 6", "genre": "turn-based-strategy", "age": "12", "platform": "pc"},
    {"title": "Resident Evil Village", "genre": "survival-horror", "age": "18", "platform": "playstation"},
    {"title": "XCOM 2", "genre": "turn-based-strategy", "age": "16", "platform": "pc"},
    {"title": "Age of Empires IV", "genre": "real-time-strategy", "age": "12", "platform": "pc"},
    {"title": "Amnesia: Rebirth", "genre": "psychological-horror", "age": "16", "platform": "pc"},
    {"title": "Crusader Kings III", "genre": "turn-based-strategy", "age": "12", "platform": "pc"},
    {"title": "Resident Evil 7", "genre": "survival-horror", "age": "18", "platform": "playstation"},
    {"title": "Five Nights at Freddy's: Security Breach", "genre": "survival-horror", "age": "12", "platform": "pc"},
    {"title": "Plague Inc: Evolved", "genre": "turn-based-strategy", "age": "12", "platform": "pc"},
    {"title": "Silent Hill 2 Remake", "genre": "psychological-horror", "age": "18", "platform": "playstation"},
    {"title": "Hearts of Iron IV", "genre": "turn-based-strategy", "age": "12", "platform": "pc"},


    # Sandbox
    {"title": "Minecraft", "genre": "sandbox-survival", "age": "7", "platform": "nintendo switch"},
    {"title": "Terraria", "genre": "sandbox-survival", "age": "7", "platform": "pc"},
    {"title": "No Man's Sky", "genre": "sandbox-survival", "age": "7", "platform": "playstation"},
    {"title": "Valheim", "genre": "sandbox-survival", "age": "12", "platform": "pc"},
    {"title": "Garry's Mod", "genre": "sandbox", "age": "12", "platform": "pc"},
    {"title": "Roblox", "genre": "sandbox", "age": "7", "platform": "mobile"},
    {"title": "Stardew Valley", "genre": "sandbox-survival", "age": "3", "platform": "nintendo switch"},
    {"title": "Cities: Skylines", "genre": "sandbox", "age": "3", "platform": "pc"},
    {"title": "Rust", "genre": "sandbox-survival", "age": "18", "platform": "pc"},
    {"title": "ARK: Survival Evolved", "genre": "sandbox-survival", "age": "16", "platform": "xbox"},
    {"title": "Planet Zoo", "genre": "sandbox", "age": "3", "platform": "pc"},
    
    # Shooter Variants
    {"title": "Gears of War", "genre": "third-person-shooter", "age": "18", "platform": "xbox"},
    {"title": "Splatoon 3", "genre": "third-person-shooter", "age": "12", "platform": "nintendo switch"},
    {"title": "Rainbow six siege", "genre": "tactical-shooter", "age": "18", "platform": "playstation"},
    {"title": "Marvel Rivals", "genre": "hero-shooter", "age": "12", "platform": "pc"},
    {"title": "Overwatch", "genre": "hero-shooter", "age": "12", "platform": "pc"},
    {"title": "Warframe", "genre": "third-person-shooter", "age": "16", "platform": "pc"},
    {"title": "Destiny 2", "genre": "hero-shooter", "age": "16", "platform": "playstation"},
    {"title": "Deep Rock Galactic", "genre": "tactical-shooter", "age": "12", "platform": "xbox"},
    {"title": "Paladins", "genre": "hero-shooter", "age": "12", "platform": "nintendo switch"},
    {"title": "The Division 2", "genre": "tactical-shooter", "age": "18", "platform": "xbox"},
    {"title": "Helldivers 2", "genre": "third-person-shooter", "age": "16", "platform": "playstation"},
    {"title": "Borderlands 2", "genre": "third-person-shooter", "age": "18", "platform": "pc"},
    {"title": "Fortnite Save the World", "genre": "third-person-shooter", "age": "12", "platform": "xbox"},
    {"title": "Team Fortress 2", "genre": "hero-shooter", "age": "12", "platform": "pc"},
    {"title": "Ghost Recon Wildlands", "genre": "tactical-shooter", "age": "18", "platform": "playstation"},

    # Battle Royale
    {"title": "Apex Legends", "genre": "battle-royale", "age": "16", "platform": "playstation"},
    {"title": "Playerunknown's battlegrounds", "genre": "battle-royale", "age": "16", "platform": "pc"},
    {"title": "Hunt showdown 1896", "genre": "battle-royale", "age": "18", "platform": "pc"},
    {"title": "TABG", "genre": "battle-royale", "age": "12", "platform": "pc"},
    {"title": "super animal royale", "genre": "battle-royale", "age": "12", "platform": "nintendo switch"},
    {"title": "Fortnite", "genre": "battle-royale", "age": "12", "platform": "playstation"},
    {"title": "Warzone", "genre": "battle-royale", "age": "18", "platform": "xbox"},
    {"title": "Naraka: Bladepoint", "genre": "battle-royale", "age": "16", "platform": "pc"},
    {"title": "The Finals", "genre": "battle-royale", "age": "16", "platform": "pc"},
    {"title": "Ring of Elysium", "genre": "battle-royale", "age": "16", "platform": "pc"},
    
    # RPG
    {"title": "Elden Ring", "genre": "rpg", "age": "18", "platform": "pc"},
    {"title": "Monster Hunter World", "genre": "rpg", "age": "16", "platform": "pc"},
    {"title": "Assassin's Creed Shadows", "genre": "rpg", "age": "18", "platform": "xbox"},
    {"title": "Cyberpunk 2077", "genre": "rpg", "age": "18", "platform": "playstation"},
    {"title": "Dark Souls III", "genre": "rpg", "age": "16", "platform": "pc"},
    {"title": "The Witcher 3", "genre": "rpg", "age": "18", "platform": "pc"},
    {"title": "Final Fantasy XVI", "genre": "rpg", "age": "18", "platform": "playstation"},
    {"title": "Dragon Age: Inquisition", "genre": "rpg", "age": "16", "platform": "xbox"},

    # Racing
    {"title": "Forza Horizon 5", "genre": "racing", "age": "3", "platform": "xbox"},
    {"title": "Gran Turismo 7", "genre": "racing", "age": "3", "platform": "playstation"},
    {"title": "Need for Speed Heat", "genre": "racing", "age": "12", "platform": "pc"},
    {"title": "F1 24", "genre": "racing", "age": "3", "platform": "playstation"},
    {"title": "Crash Team Racing Nitro-Fueled", "genre": "racing", "age": "3", "platform": "nintendo switch"},
    {"title": "Dirt Rally 2.0", "genre": "racing", "age": "3", "platform": "pc"},
    {"title": "Burnout Paradise Remastered", "genre": "racing", "age": "7", "platform": "xbox"},

    # Indie
    {"title": "Celeste", "genre": "indie", "age": "7", "platform": "nintendo switch"},
    {"title": "Hades II", "genre": "indie", "age": "16", "platform": "pc"},
    {"title": "Stardew Valley", "genre": "indie", "age": "3", "platform": "pc"},
    {"title": "Cuphead", "genre": "indie", "age": "7", "platform": "xbox"},
    {"title": "Undertale", "genre": "indie", "age": "7", "platform": "pc"},
    {"title": "Little Nightmares II", "genre": "indie", "age": "12", "platform": "playstation"},
    {"title": "Spiritfarer", "genre": "indie", "age": "7", "platform": "nintendo switch"},

    # RTS
    {"title": "StarCraft II", "genre": "rts", "age": "12", "platform": "pc"},
    {"title": "Age of Empires II: Definitive Edition", "genre": "rts", "age": "12", "platform": "pc"},
    {"title": "Halo Wars 2", "genre": "rts", "age": "16", "platform": "xbox"},
    {"title": "Company of Heroes 3", "genre": "rts", "age": "16", "platform": "pc"},
    {"title": "Warcraft III: Reforged", "genre": "rts", "age": "12", "platform": "pc"},
    {"title": "Iron Harvest", "genre": "rts", "age": "12", "platform": "playstation"},
    {"title": "They Are Billions", "genre": "rts", "age": "12", "platform": "pc"},

    #Story-Driven
    {"title": "The Walking Dead: Season 1", "genre": "story", "age": "18", "platform": "pc"},
    {"title": "Detroit: Become Human", "genre": "story", "age": "18", "platform": "playstation"},
    {"title": "Life is Strange", "genre": "story", "age": "16", "platform": "pc"},
    {"title": "Firewatch", "genre": "story", "age": "16", "platform": "xbox"},
    {"title": "What Remains of Edith Finch", "genre": "story", "age": "12", "platform": "playstation"},
    {"title": "Oxenfree", "genre": "story", "age": "12", "platform": "nintendo switch"},
    {"title": "Resident Evil 4 Remake", "genre": "story", "age": "18", "platform": "playstation"},
]


satisfied = False #variabel för att hålla reda på om användare är nöjd med rekommendationerna eller inte, startar som false för att programmet ska kunna rekomendera 
shown_games = []

def save_favorite(favorite_game): #funktion för att spara favoritspel till en fil
   
    with open("favorite_game.txt", "a") as file:  # "a"för att lägga till i filen med spel istället för att skriva över varje gång man startar om programmet
        file.write(f"\nFavorite Game: {favorite_game}\n")
        file.write(f"Genre: {genre}\n")
        file.write(f"Platform: {platform}\n")
        file.write(f"Age Limit: {age}\n")
        file.write("-" * 50 + "\n")
    print(f"\nYour favorite '{favorite_game}' has been saved to 'favorite_game.txt'!") #skriver ut att favorit spelet har sparats

def display_saved_games(): #visar sparade spel från filen "favorite_game.txt"
    """Visa sparade spel från fil"""
    try:
        with open("favorite_game.txt", "r") as file: 
            print("\n" + "="*50)
            print("YOUR CURRENTLY SAVED GAMES:")
            print("="*50)
            print(file.read())
            print("="*50 + "\n")
    except FileNotFoundError:
        print("\nNo saved games found.\n")

def find_games(): #går igenom listan med spel och rekommenderar de som matchar användarens önskemål
    global satisfied
    
    while not satisfied: # while loop för att fortsätta rekommendera spel tills användaren är nöjd
        matched_games = []  # lista för att spara alla matchningar med poäng
        
        for game in games:  
            score = 0
            
            if game["age"] == age:
                score += 1
            if game["platform"].lower() == platform:
                score += 1
            if genre in game["genre"].lower():
                score += 2
            
            # Om spelet matchar minst 2 kriterier och inte redan visats, lägg till i lista
            if score >= 2 and game["title"] not in shown_games:
                matched_games.append({"title": game["title"], "score": score})  # Spara både titel och poäng
        
        #  Sortera efter poäng (högsta först) - key=lambda säger "sortera efter score-värdet"
        matched_games.sort(key=lambda x: x["score"], reverse=True)
        
        # Ta bara de 4 första med  högsta poäng)
        current_recommendations = []
        for game in matched_games[:4]:  # tar bara första 4 elementen
            print(game["title"])
            current_recommendations.append(game["title"])
        
        shown_games.extend(current_recommendations) # Lägg till de rekommenderade spelen i shown_games
        
        if len(current_recommendations) == 0: # Om inga nya rekommendationer hittas
            print("Sorry, I couldn't find any more games that match your preferences.")
            satisfied = True
        else:
            print("My recommendation for you is: " + str(len(current_recommendations)) + " titles")
            answer = input("Are you satisfied with the recommendations? (yes/no) ").lower()  
            if answer == "yes":
                satisfied = True
                print("Great! Enjoy your gaming!")
                
                favorite = input("Which one did you like the best? (type the game title): ").strip()
                
                if favorite in current_recommendations:
                    save_favorite(favorite)
                else:
                    print(f"'{favorite}' was not in the recommendations. Please try again.")

if __name__ == "__main__":
    find_games()
    display_saved_games()  #  Visa sparade spel innan programmet avslutas