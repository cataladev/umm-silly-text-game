# commands.py
from trie import CommandTrie
from actions import *

def setup_commands():
    trie = CommandTrie()
    
    # Universal commands (available everywhere)
    trie.insert(["quit"], ["*"], quit_game, "Quit the game.")
    trie.insert(["inventory"], ["*"], show_inventory, "Check your inventory.")
    trie.insert(["map"], ["*"], check_map, "Show this help message.")
    trie.insert(["lore"], ["*"], lore, "Show the game's lore.")
    
    # House commands
    trie.insert(["sleep"], ["house"], sleep, "Honk shuu.")
    trie.insert(["bertha"], ["house"], bertha, "Play with Bertha.")
    trie.insert(["go", "farm"], ["house"], go_farm, "Go to your farm.")
    trie.insert(["go", "town"], ["house"], go_town, "Travel to the town.")
    
    # Farm commands
    trie.insert(["plant", "wheat"], ["farm"], lambda game: game.plant("wheat", 1), "Plant wheat seeds.")
    trie.insert(["plant", "corn"], ["farm"], lambda game: game.plant("corn", 1), "Plant corn seeds.")
    trie.insert(["water"], ["farm"], lambda game: game.water(), "Water your crops.")
    trie.insert(["harvest"], ["farm"], lambda game: game.harvest(), "Harvest fully grown crops.")
    
    # Travel commands
    trie.insert(["go", "house"], ["farm", "town"], go_house, "Return home.")
    
    # Town commands
    trie.insert(["buy", "seeds"], ["town"], buy_seeds, "Buy wheat seeds for your farm.")
    trie.insert(["sell", "wheat"], ["town"], sell_wheat, "Sell wheat for gold.")
    
    return trie