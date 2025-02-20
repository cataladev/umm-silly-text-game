from game_state import GameState
from commands import setup_commands
from actions import show_help

def game_loop():
    game = GameState()
    command_trie = setup_commands()
    print(f"Welcome to the \033[31mFarming\033[0m Game!")
    print("Type 'help' for a list of commands.")
    print("Type 'quit' to exit the game.")
    print("Type 'inventory' to check your inventory.")
    print("=== Day 1 Begins ===")
    while True:
        print(f"\nDay {game.day} - {game.format_time()} - You're in your {game.location}.")
        command = input("> ").strip().lower().split()
        
        if command == ["help"]:
            show_help(game, command_trie)
            continue
        
        action = command_trie.search(command, game.location)
        
        if action:
            action(game)
            if game.time == 360 and game.day > 1:
                print(f"\n=== Day {game.day} Begins ===")
        else:
            print("Invalid command or not allowed here!")

if __name__ == "__main__":
    game_loop()