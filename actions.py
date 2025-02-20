from game_state import GameState
from vars import *
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
    sorted_commands = sorted(commands, key=lambda x: x[0])
    
    for cmd, desc in sorted_commands:
        print(f"> {BLUE}{cmd}{RESET}: {YELLOW}{desc}{RESET}")
    print(f"> {BLUE}help{RESET}: {YELLOW}Show this help message.{RESET}")

def check_map(game: GameState):
    print("You look at your map.")
    print("Farm: A small plot of land outside.")
    print("House: Your cozy home.")

def lore(game:GameState):
    match game.location:

        case "house":

            print("This house has been in your family for generations.")
            print("Your parents left it to you, hoping you'll make a good life here.")
            print("After your parents died, your brother set out to the dungeons, and never returned.")
            print("You often wonder what happened to him.")

        case "farm":

            print("You remember your grandpa telling you stories about this land.")
            print("He said the soil is enchanted, perfect for growing crops.")
            print("With the right care, your farm will thrive.")
            print("The farm has been in your family for generations, passed down with love and care.")

        case "town":
            print("The town has a rich history, this town is a hub for adventures and traders.")
            print("The nearby dungeons and caves are rumored to be filled with treasures, few return from them.")
            print("The town is a place of opportunity, where dreams can come true.")

    
#==================Travelling actions==========================
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
    game.add_time(30)
    print("You travel to the town.")


#===========================Town Actions============================
def buy_seeds(game: GameState):
    if game.inventory["gold"] >= 20:
        game.inventory["gold"] -= 20
        game.inventory["crop seeds"]["wheat"] += 5
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
def sleep(game: GameState):
    game.add_time(1320)  # max time, resets day
    print("You had a good night's sleep.")

def bertha(game: GameState):
    print("You play with your dog, Bertha.")
    game.add_time(15)



#Town Actions

