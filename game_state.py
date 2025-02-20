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
            print("\n=== Day ends at 22:00 ===")
            self.day += 1
            self.time = 360  # Reset to 6:00 AM
            self.location = "house"
            self.farm["watered"] = False  # Reset watering status for the new day
        else:
            self.time += minutes
            if self.time >= 1320:
                self.add_time(0)