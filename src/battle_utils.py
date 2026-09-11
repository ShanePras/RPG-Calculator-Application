import random
import math

class Battler:
    def __init__(self, stats: list):
        self.name = stats[0]
        self.label = stats[1]
        self.hp = stats[2]
        self.max_hp = stats[3]
        self.mp = 0
        self.max_mp = stats[4]
        self.strength = stats[5]
        self.magic = stats[6]
        self.defense = stats[7]
        self.agility = stats[8]
        self.luck = stats[9]
        self.slash_resist = stats[10]
        self.strike_resist = stats[11]
        self.pierce_resist = stats[12]
        self.fire_resist = stats[13]
        self.water_resist = stats[14]
        self.lightning_resist = stats[15]
        self.earth_resist = stats[16]
        self.wind_resist = stats[17]
        self.other_resist = stats[18]
        self.attack_level = 0 #integer from -3 to 3 inclusive
        self.defense_level = 0 #integer from -3 to 3 inclusive
        self.agility_level = 0 #integer from -3 to 3 inclusive
        self.formation = True #bool. True means forward, False means back
        self.guard = False 
        self.charge = False
        self.status = "None" #string