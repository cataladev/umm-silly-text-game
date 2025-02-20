from trie import CommandTrie
from actions import go_house, go_farm, go_town, buy_seeds, sell_wheat, quit_game, show_inventory

def setup_commands():
    trie = CommandTrie()
    
    # Universal commands
    trie.insert(["quit"], ["house", "farm", "town"], quit_game, "Quit the game.")  # Add quit command
    trie.insert(["inventory"], ["house", "farm", "town"], show_inventory, "Check your inventory.")  # Dummy action
    
    # House commands
    trie.insert(["go", "home"], ["farm", "town"], go_house, "Return home from anywhere.")
    trie.insert(["go", "farm"], ["house"], go_farm, "Go to your farm.")
    trie.insert(["go", "town"], ["house"], go_town, "Travel to the town.")
    
    # Town commands
    trie.insert(["buy", "seeds"], ["town"], buy_seeds, "Buy wheat seeds for your farm.")
    trie.insert(["sell", "wheat"], ["town"], sell_wheat, "Sell 5 wheat for gold.")

    # Farm commands

    
    return trie