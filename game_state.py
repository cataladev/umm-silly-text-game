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

    def plant(self, crop: str, plots: int):
        if self.location != "farm":
            print("You can only plant crops on the farm!")
            return
        
        if crop not in self.inventory["crop seeds"]:
            print(f"You don't have any {crop} seeds!")
            return
        
        if plots > self.farm["plots"]:
            print(f"You only have {self.farm['plots']} plots available!")
            return
        
        if self.inventory["crop seeds"][crop] < plots:
            print(f"You don't have enough {crop} seeds to plant {plots} plots!")
            return
        
        # Deduct seeds and allocate plots
        self.inventory["crop seeds"][crop] -= plots
        self.farm["growing"][crop]["plots"] += plots
        self.farm["plots"] -= plots
        self.add_time(15)  # Planting takes 15 minutes
        print(f"Planted {plots} plots of {crop}.")

    def water(self):
        if self.location != "farm":
            print("You can only water crops on the farm!")
            return
        
        if self.farm["watered"]:
            print("You've already watered the crops today!")
            return
        
        # Advance growth stage for all crops
        for crop in self.farm["growing"]:
            if self.farm["growing"][crop]["plots"] > 0:
                self.farm["growing"][crop]["stage"] += 1
                print(f"Watered {self.farm['growing'][crop]['plots']} plots of {crop}.")
        
        self.farm["watered"] = True
        self.add_time(30)  # Watering takes 30 minutes

    def harvest(self):
        if self.location != "farm":
            print("You can only harvest crops on the farm!")
            return
        
        harvested = False
        for crop in self.farm["growing"]:
            if self.farm["growing"][crop]["stage"] >= 3:  # Crops are fully grown at stage 3
                plots = self.farm["growing"][crop]["plots"]
                self.inventory["crop"][crop] += plots * 5  # Each plot yields 5 crops
                self.farm["plots"] += plots
                self.farm["growing"][crop] = {"stage": 0, "plots": 0}  # Reset growth
                print(f"Harvested {plots} plots of {crop}!")
                harvested = True
        
        if not harvested:
            print("No crops are ready to harvest yet.")
        self.add_time(30)  # Harvesting takes 30 minutes