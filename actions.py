from game_state import GameState
from vars import *

# Universal actions
def quit_game(game: GameState):
    print("Thanks for playing! Goodbye!")
    exit()

def show_inventory(game: GameState):
    print("\n=== Inventory ===")
    print(f"Gold: {game.inventory['gold']}")
    print("Crops:")
    for crop, amount in game.inventory["crop"].items():
        print(f"  {crop.capitalize()}: {amount}")
    print("Crop Seeds:")
    for crop, amount in game.inventory["crop seeds"].items():
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
    print("\nYou look at your map.")
    print("House: Your cozy home.")
    print("Farm: A small plot of land outside.")
    print("Town: A bustling place with shops and people.")

def lore(game: GameState):
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

# ================== Travelling actions ==========================
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

# =========================== Town Actions =============================
def buy_seeds(game: GameState, amount: str = "5"):
    try:
        amount = int(amount)  # Convert parameter to integer
    except ValueError:
        print("Invalid amount!")
        return
    
    if game.location != "town":
        print("You can only buy seeds in town!")
        return
    
    total_cost = amount * 4  # Assume seeds cost 4 gold each
    if game.inventory["gold"] < total_cost:
        print(f"You don't have enough gold to buy {amount} seeds!")
        return
    
    game.inventory["gold"] -= total_cost
    game.inventory["crop seeds"]["wheat"] += amount
    game.add_time(15)  # Buying takes 15 minutes
    print(f"Bought {amount} wheat seeds for {total_cost} gold!")

def sell_wheat(game: GameState, amount: str = "5"):
    try:
        amount = int(amount)  # Convert parameter to integer
    except ValueError:
        print("Invalid amount!")
        return
    
    if game.location != "town":
        print("You can only sell wheat in town!")
        return
    
    if game.inventory["crop"]["wheat"] < amount:
        print(f"You don't have enough wheat to sell {amount}!")
        return
    
    game.inventory["crop"]["wheat"] -= amount
    game.inventory["gold"] += amount * 3  # Sell price: 3 gold per wheat
    game.add_time(15)  # Selling takes 15 minutes
    print(f"Sold {amount} wheat for {amount * 3} gold!")

# =========================== Farm Actions =============================
def plant(game: GameState, crop: str, plots: str = "1"):
    try:
        plots = int(plots)  # Convert parameter to integer
    except ValueError:
        print("Invalid number of plots!")
        return
    
    if game.location != "farm":
        print("You can only plant crops on the farm!")
        return
    
    if crop not in game.inventory["crop seeds"]:
        print(f"You don't have any {crop} seeds!")
        return
    
    if plots > game.farm["plots"]:
        print(f"You only have {game.farm['plots']} plots available!")
        return
    
    if game.inventory["crop seeds"][crop] < plots:
        print(f"You don't have enough {crop} seeds to plant {plots} plots!")
        return
    
    # Deduct seeds and allocate plots
    game.inventory["crop seeds"][crop] -= plots
    game.farm["growing"][crop]["plots"] += plots
    game.farm["plots"] -= plots
    game.add_time(15)  # Planting takes 15 minutes
    print(f"Planted {plots} plots of {crop}.")

def water(game: GameState):
    if game.location != "farm":
        print("You can only water crops on the farm!")
        return
    
    if game.farm["watered"]:
        print("You've already watered the crops today!")
        return
    
    # Advance growth stage for all crops
    for crop in game.farm["growing"]:
        if game.farm["growing"][crop]["plots"] > 0:
            game.farm["growing"][crop]["stage"] += 1
            print(f"Watered {game.farm['growing'][crop]['plots']} plots of {crop}.")
    
    game.farm["watered"] = True
    game.add_time(30)  # Watering takes 30 minutes

def harvest(game: GameState):
    if game.location != "farm":
        print("You can only harvest crops on the farm!")
        return
    
    harvested = False
    for crop in game.farm["growing"]:
        if game.farm["growing"][crop]["stage"] >= 3:  # Crops are fully grown at stage 3
            plots = game.farm["growing"][crop]["plots"]
            game.inventory["crop"][crop] += plots * 5  # Each plot yields 5 crops
            game.farm["plots"] += plots
            game.farm["growing"][crop] = {"stage": 0, "plots": 0}  # Reset growth
            print(f"Harvested {plots} plots of {crop}!")
            harvested = True
    
    if not harvested:
        print("No crops are ready to harvest yet.")
    game.add_time(30)  # Harvesting takes 30 minutes

# =========================== House Actions =============================
def sleep(game: GameState):
    game.add_time(1320)  # max time, resets day
    print("You had a good night's sleep.")

def bertha(game: GameState):
    print("You play with your dog, Bertha.")
    game.add_time(15)