import random
import math

#Settings is a seperate class so people can change multipliers, and they can apply to other battlers.
#I personally like the scaling to be consistent between levels, but others might think/want otherwise.
class BattleSettings:
    def __init__(self):
        self.l_atk_mtplr = 1.3 #light attack multiplier
        self.m_atk_mtplr = 1.9 #medium attack multiplier
        self.h_atk_mtplr = 2.6 #heavy attack multiplier
        self.s_atk_mtplr = 3.2 #severe attack multiplier
        self.c_atk_mtplr = 3.6 #colossal attack multiplier

        self.res_weak_mtplr = 1.5 #resistance WEAK multiplier
        self.res_res_mtplr = 0.5 #resistance RESIST multiplier

        self.buff_1_mtplr = 1.25 #buff level 1 multiplier
        self.buff_2_mtplr = 1.5 #buff level 2 multiplier
        self.buff_3_mtplr = 1.75 #buff level 3 multiplier
        self.buff_n1_mtplr = 0.75 #buff level -1 multiplier
        self.buff_n2_mtplr = 0.5 #buff level -2 multiplier
        self.buff_n3_mtplr = 0.25 #buff level -3 multiplier

        self.form_b_mtplr = 0.6 #form back multiplier

        self.charge_mtplr = 2.2 #charge multiplier

        self.guard_mtplr = 2.0 #guard multiplier

        self.atk_const = 2.57 #attack constant
        self.ddg_const = 0.15 #dodge constant
        self.crt_const = 0.1 #critical constant

        self.heal_l_mtplr = 3.5 #light heal multiplier
        self.heal_m_mtplr = 5.0 #medium heal multiplier
        self.heal_h_mtplr = 6.5 #heavy heal multiplier

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
        #All "resists" control what kinds of attacks characters can resist or not resist.
        #0-Normal, 1-Weak, 2-Resists, 3-Null, 4-Reflect, 5-Drain
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

