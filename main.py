from game_state import GameState
from commands import setup_commands
from actions import show_help
from vars import *

def game_loop():
    game = GameState()
    command_trie = setup_commands()
    print(f"Welcome to the{RED} Game! {RESET}")
    print("Explore the map, things will grow and appear as the days go by.")
    print("Type 'inventory' to check your inventory.")
    print("Type 'help' for a list of commands.")
    print("Type 'quit' to exit the game.")  
    while True:
        print(f"\n{game.format_time()} - You're in your {game.location}.")
        user_input = input("> ").strip().lower()
        command_parts = user_input.split()
        
        if not command_parts:
            continue
        
        command = command_parts[0]
        params = command_parts[1:]  # Extract parameters
        
        if command == "help":
            show_help(game, command_trie)
            continue
        
        # Search for the command in the Trie
        action = command_trie.search(command_parts, game.location)
        
        if action:
            try:
                action(game, *params)  # Pass parameters to the action
            except TypeError as e:
                print(f"Invalid usage: {e}")
        else:
            print("Invalid command or not allowed here!")

if __name__ == "__main__":
    game_loop()