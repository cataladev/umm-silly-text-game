from trie import CommandTrie
from actions import *

def setup_commands():
    trie = CommandTrie()
    
    # Universal commands (available everywhere)
    trie.insert(["quit"], ["*"], quit_game, "Quit the game.")
    trie.insert(["inventory"], ["*"], show_inventory, "Check your inventory.")
    trie.insert(["map"], ["*"], check_map, "Show this help message.")
    trie.insert(["lore"], ["*"], lore, "Show the game's lore.")
    trie.insert(["save"], ["*"], lambda game, *_: game.save_game(), "Save the game.")
    trie.insert(["load"], ["*"], lambda game, *_: GameState.load_game(), "Load the game.")
    
    # House commands
    trie.insert(["sleep"], ["house"], sleep, "Honk shuu.")
    trie.insert(["bertha"], ["house"], bertha, "Play with Bertha.")
    trie.insert(["go", "farm"], ["house"], go_farm, "Go to your farm.")
    trie.insert(["go", "town"], ["house"], go_town, "Travel to the town.")
    
    # Farm commands
    trie.insert(["plant", "wheat"], ["farm"], lambda game, *params: plant(game, "wheat", *params), "Plant wheat seeds. Usage: plant wheat [plots]")
    trie.insert(["plant", "corn"], ["farm"], lambda game, *params: plant(game, "corn", *params), "Plant corn seeds. Usage: plant corn [plots]")
    trie.insert(["water"], ["farm"], lambda game, *_: water(game), "Water your crops.")
    trie.insert(["harvest"], ["farm"], lambda game, *_: harvest(game), "Harvest fully grown crops.")
    trie.insert(["check", "plots"], ["farm"], lambda game, *_: check_plots(game), "Check crop growth status.")
    
    # Travel commands
    trie.insert(["go", "house"], ["farm", "town"], go_house, "Return home.")
    
    # Town commands
    trie.insert(["buy", "seeds"], ["town"], lambda game, *params: buy_seeds(game, *params), "Buy wheat seeds. Usage: buy seeds [amount]")
    trie.insert(["sell", "wheat"], ["town"], lambda game, *params: sell_wheat(game, *params), "Sell wheat. Usage: sell wheat [amount]")
    
    return trie