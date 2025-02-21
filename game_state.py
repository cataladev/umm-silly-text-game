import json

class GameState:
    def __init__(self):
        self.day = 1
        self.time = 360  # 6:00 AM in minutes (6*60)
        self.location = "house"
        self.inventory = {
            "gold": 100,
            "crop": {"wheat": 10, "corn": 0},
            "crop seeds": {"wheat": 0, "corn": 0},
            "equipment": []
        }
        self.farm = {
            "growing": {"wheat": {"stage": 0, "plots": 0}, "corn": {"stage": 0, "plots": 0}},  # Track growth stage and plots used
            "plots": 5,  # Total available plots
            "watered": False  # Track if crops have been watered today
        }
    
    def format_time(self):
        hours = self.time // 60
        minutes = self.time % 60
        return f"{hours:02d}:{minutes:02d}"

    def add_time(self, minutes):
        if self.time >= 1320:  # 22*60 = 1320
            if self.location == "town":  # If you're in town, you get robbed
                print("You stayed out too late and got robbed! You lost 20 gold.")
                self.inventory["gold"] -= 20
            print(f"\n=== Day {self.day} ends at 22:00 ===")
            self.day += 1
            self.time = 360  # Reset to 6:00 AM
            self.location = "house"
            self.farm["watered"] = False  # Reset watering status for the new day
            print(f"=== Day {self.day} begins at 6:00 ===")
        else:
            self.time += minutes
            if self.time >= 1320:
                self.add_time(0)
    
    #save files..?!?!?
    def to_dict(self):
        """Convert the GameState to a JSON-serializable dictionary."""
        return {
            "day": self.day,
            "time": self.time,
            "location": self.location,
            "inventory": self.inventory,
            "farm": self.farm
        }

    @classmethod
    def from_dict(cls, data):
        #Create a GameState from a dictionary.
        game = cls()
        game.day = data["day"]
        game.time = data["time"]
        game.location = data["location"]
        game.inventory = data["inventory"]
        game.farm = data["farm"]
        return game

    def save_game(self, filename="save.json"):
        #Save the game state to a JSON file.
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=2)
        print(f"Game saved to {filename}.")

    @classmethod
    def load_game(cls, filename="save.json"):
        #Load a game state from a JSON file.
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            print(f"Game loaded from {filename}.")
            return cls.from_dict(data)
        except FileNotFoundError:
            print("No save file found. Starting a new game.")
            return cls()
        except json.JSONDecodeError:
            print("Corrupted save file. Starting a new game.")
            return cls()