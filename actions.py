from game_state import GameState

#Universal actions
def quit_game(game: GameState):
    print("Thanks for playing! Goodbye!")
    exit()

def show_inventory(game: GameState):
    print("\n=== Inventory ===")
    print(f"Gold: {game.inventory['gold']}")
    print("Crops:")
    for crop, amount in game.inventory["crops"].items():
        print(f"  {crop.capitalize()}: {amount}")
    print("Equipment:")
    if game.inventory["equipment"]:
        for item in game.inventory["equipment"]:
            print(f"  {item}")
    else:
        print("  None")

def show_help(game: GameState, command_trie):
    print("\n=== Available Commands ===")
    commands = command_trie.get_all_commands(game.location)
    for cmd, desc in commands:
        print(f"> {cmd}: {desc}")
    print("> help: Show this help message.")
    
#Travelling actions
def go_house(game: GameState, minutes=30):
    game.location = "house"
    game.add_time(minutes)
    print(f"You return home.")

def go_farm(game: GameState):
    game.location = "farm"
    game.add_time(30)
    print("You head to the farm.")

def go_town(game: GameState):
    game.location = "town"
    game.add_time(300)
    print("You travel to the town.")


#Farm Actions
def buy_seeds(game: GameState):
    if game.inventory["gold"] >= 20:
        game.inventory["gold"] -= 20
        game.inventory["crops"]["wheat"] += 5
        game.add_time(15)
        print("Bought 5 wheat seeds!")
    else:
        print("Not enough gold!")

def sell_wheat(game: GameState):
    if game.inventory["crops"]["wheat"] >= 5:
        game.inventory["crops"]["wheat"] -= 5
        game.inventory["gold"] += 15
        game.add_time(15)
        print("Sold 5 wheat!")
    else:
        print("Not enough wheat!")

#House Actions

#Town Actions

