# commands.py
from trie import CommandTrie
from actions import *

def setup_commands():
    trie = CommandTrie()
    
    # Universal commands (available everywhere)
    trie.insert(["quit"], ["*"], lambda game, *_: quit_game(game), "Quit the game.")
    trie.insert(["inventory"], ["*"], lambda game, *_: show_inventory(game), "Check your inventory.")
    trie.insert(["map"], ["*"], lambda game, *_: check_map(game), "Show this help message.")
    trie.insert(["lore"], ["*"], lambda game, *_: lore(game), "Show the game's lore.")
    
    # House commands
    trie.insert(["sleep"], ["house"], lambda game, *_: sleep(game), "Honk shuu.")
    trie.insert(["bertha"], ["house"], lambda game, *_: bertha(game), "Play with Bertha.")
    trie.insert(["go", "farm"], ["house"], lambda game, *_: go_farm(game), "Go to your farm.")
    trie.insert(["go", "town"], ["house"], lambda game, *_: go_town(game), "Travel to the town.")
    
    # Farm commands
    trie.insert(["plant", "wheat"], ["farm"], lambda game, *params: plant(game, "wheat", *params), "Plant wheat seeds. Usage: plant wheat [plots]")
    trie.insert(["plant", "corn"], ["farm"], lambda game, *params: plant(game, "corn", *params), "Plant corn seeds. Usage: plant corn [plots]")
    trie.insert(["water"], ["farm"], lambda game, *_: water(game), "Water your crops.")
    trie.insert(["harvest"], ["farm"], lambda game, *_: harvest(game), "Harvest fully grown crops.")
    
    # Travel commands
    trie.insert(["go", "house"], ["farm", "town"], lambda game, *_: go_house(game), "Return home.")
    
    # Town commands
    trie.insert(["buy", "seeds"], ["town"], lambda game, *params: buy_seeds(game, *params), "Buy wheat seeds. Usage: buy seeds [amount]")
    trie.insert(["sell", "wheat"], ["town"], lambda game, *params: sell_wheat(game, *params), "Sell wheat. Usage: sell wheat [amount]")
    
    return trie