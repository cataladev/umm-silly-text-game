from trie import CommandTrie
from actions import go_house, go_farm, go_town, buy_seeds, sell_wheat, quit_game, show_inventory

def setup_commands():
    trie = CommandTrie()
    
    # Universal commands (available everywhere)
    trie.insert(["quit"], ["*"], quit_game, "Quit the game.")
    trie.insert(["inventory"], ["*"], show_inventory, "Check your inventory.")
    
    # House commands
    trie.insert(["go", "farm"], ["house"], go_farm, "Go to your farm.")
    trie.insert(["go", "town"], ["house"], go_town, "Travel to the town.")
    
    # Town commands
    trie.insert(["buy", "seeds"], ["town"], buy_seeds, "Buy wheat seeds for your farm.")
    trie.insert(["sell", "wheat"], ["town"], sell_wheat, "Sell wheat for gold.")

    #Farm commands

    return trie
