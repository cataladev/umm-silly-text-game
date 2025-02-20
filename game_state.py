class GameState:
    def __init__(self):
        self.day = 1
        self.time = 360  # 6:00 AM in minutes (6*60)
        self.location = "house"
        self.inventory = {
            "gold": 100,
            "crops": {"wheat": 0, "corn": 0},
            "equipment": []
        }

    def format_time(self):
        hours = self.time // 60
        minutes = self.time % 60
        return f"{hours:02d}:{minutes:02d}"

    def add_time(self, minutes):
        self.time += minutes
        # End day at 22:00 (10 PM)
        if self.time >= 1320:  # 22*60 = 1320
            if self.location == "town":
                print("You stayed out too late and got robbed! You lost 20 gold.")
                self.inventory["gold"] -= 20
            print("\n--- Day ends at 22:00 ---")
            self.day += 1
            self.time = 360  # Reset to 6:00 AM
            self.location = "house"
            