import random
import math

#Settings is a seperate class so people can change multipliers, and they can apply to other battlers.
#I personally like the scaling to be consistent between levels, but others might think/want otherwise.
class BattleSettings:
    def __init__(self):
        self.set_lst = []

        self.set_lst.append(1.3) #light attack multiplier; 0
        self.set_lst.append(1.9) #medium attack multiplier; 1
        self.set_lst.append(2.6) #heavy attack multiplier; 2
        self.set_lst.append(3.2) #severe attack multiplier; 3
        self.set_lst.append(3.6) #colossal attack multiplier; 4

        self.set_lst.append(1.5) #resistance WEAK multiplier; 5
        self.set_lst.append(0.5) #resistance RESIST multiplier; 6

        self.set_lst.append(1.25) #buff level 1 multiplier; 7
        self.set_lst.append(1.5) #buff level 2 multiplier; 8
        self.set_lst.append(1.75) #buff level 3 multiplier; 9
        self.set_lst.append(0.75) #buff level -1 multiplier; 10
        self.set_lst.append(0.5) #buff level -2 multiplier; 11
        self.set_lst.append(0.25) #buff level -3 multiplier; 12

        self.set_lst.append(0.6) #form back multiplier; 13

        self.set_lst.append(2.2) #charge multiplier; 14

        self.set_lst.append(2.0) #guard multiplier; 15

        self.set_lst.append(2.57) #attack constant; 16
        self.set_lst.append(0.15) #dodge constant; 17
        self.set_lst.append(0.1) #critical constant; 18

        self.set_lst.append(3.5) #light heal multiplier; 19
        self.set_lst.append(5.0) #medium heal multiplier; 20
        self.set_lst.append(6.5) #heavy heal multiplier; 21

        self.set_lst.append(10) #light atk 1 mp; 22
        self.set_lst.append(24) #med atk 1 mp; 23
        self.set_lst.append(40) #heavy atk 1 mp; 24
        self.set_lst.append(65) #severe atk 1 mp; 25
        self.set_lst.append(100) #colossal atk 1 mp; 26

        self.set_lst.append(15) #attack all mp cost add; 27
        self.set_lst.append(3) #multiattack mp cost add; 28
        self.set_lst.append(18) #drain/splash attack mp cost add; 29
        self.set_lst.append(12) #row attack mp cost add; 30

        self.set_lst.append(0.05) #normal mp gain; 31
        self.set_lst.append(0.07) #res mp gain; 32
        self.set_lst.append(0.03) #weak mp gain; 33
        self.set_lst.append(0.1) #null mp gain; 34
        self.set_lst.append(0.15) #dodge mp gain; 35

    def getLAtkMtp(self): return self.set_lst[0]
    def getMAtkMtp(self): return self.set_lst[1]
    def getHAtkMtp(self): return self.set_lst[2]
    def getSAtkMtp(self): return self.set_lst[3]
    def getCAtkMtp(self): return self.set_lst[4]
    def getWeakMtp(self): return self.set_lst[5]
    def getResMtp(self): return self.set_lst[6]
    def getBuff1Mtp(self): return self.set_lst[7]
    def getBuff2Mtp(self): return self.set_lst[8]
    def getBuff3Mtp(self): return self.set_lst[9]
    def getBuffn1Mtp(self): return self.set_lst[10]
    def getBuffn2Mtp(self): return self.set_lst[11]
    def getBuffn3Mtp(self): return self.set_lst[12]
    def getFormMtp(self): return self.set_lst[13]
    def getChargeMtp(self): return self.set_lst[14]
    def getGuardMtp(self): return self.set_lst[15]
    def getAtkConst(self): return self.set_lst[16]
    def getDdgConst(self): return self.set_lst[17]
    def getCrtConst(self): return self.set_lst[18]
    def getLHealMtp(self): return self.set_lst[19]
    def getMHealMtp(self): return self.set_lst[20]
    def getHHealMtp(self): return self.set_lst[21]

    def getLAtkMp(self): return self.set_lst[22]
    def getMAtkMp(self): return self.set_lst[23]
    def getHAtkMp(self): return self.set_lst[24]
    def getSAtkMp(self): return self.set_lst[25]
    def getCAtkMp(self): return self.set_lst[26]
    def getAtkAllMpAdd(self): return self.set_lst[27]
    def getMultiattackMpAdd(self): return self.set_lst[28]
    def getDrnSplAtkMpAdd(self): return self.set_lst[29]
    def getRowAtkMpAdd(self): return self.set_lst[30]
    def getNorMPGain(self): return self.set_lst[31]
    def getResMPGain(self): return self.set_lst[32]
    def getWeakMPGain(self): return self.set_lst[33]
    def getNullMPGain(self): return self.set_lst[34]
    def getDodgeMPGain(self): return self.set_lst[35]

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

    def equalizeHpMp(self):
        if self.hp > self.max_hp: self.hp = self.max_hp
        if self.mp > self.max_mp: self.mp = self.max_mp
        if self.hp < 0: self.hp=0
        if self.mp < 0: self.mp=0

#ATTACK METHODS
#ATTACK INFO
def attackInfo(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", pm_phys:bool, severity:int, element:int):
    def damageCalc():
        def buffVal(buff_val:int):
            if buff_val==1: return b_settings.getBuff1Mtp()
            elif buff_val==2: return b_settings.getBuff2Mtp()
            elif buff_val==3: return b_settings.getBuff3Mtp()
            elif buff_val==-1: return b_settings.getBuffn1Mtp()
            elif buff_val==-2: return b_settings.getBuffn2Mtp()
            elif buff_val==-3: return b_settings.getBuffn3Mtp()
            else: return 1.0

        def chargeVal():
            if attacker.charge == True: return b_settings.getChargeMtp()
            else: return 1.0

        def guardVal():
            if defender.guard==True: return b_settings.getGuardMtp()
            else: return 1.0

        def atkPMVal():
            if pm_phys==True: return attacker.strength
            else: return attacker.magic

        def formAtkVal():
            if attacker.formation==True or pm_phys==False: return 1.0
            else: return b_settings.getFormMtp()

        def formDefVal():
            if defender.formation==True: return 1.0
            else: return b_settings.getFormMtp()

        def sevTypeVal():
            match severity:
                case 1: return b_settings.getLAtkMtp()
                case 2: return b_settings.getMAtkMtp()
                case 3: return b_settings.getHAtkMtp()
                case 4: return b_settings.getSAtkMtp()
                case 5: return b_settings.getCAtkMtp()
                case _: return 1.0

        def elemResVal():
            def elemDef(elem_res:int):
                match elem_res:
                    case 1: return b_settings.getWeakMtp()
                    case 2: return b_settings.getResMtp()
                    case 3: return 0.0
                    case _: return 1.0

            match element:
                case 0: return elemDef(defender.slash_resist)
                case 1: return elemDef(defender.strike_resist)
                case 2: return elemDef(defender.pierce_resist)
                case 3: return elemDef(defender.fire_resist)
                case 4: return elemDef(defender.water_resist)
                case 5: return elemDef(defender.lightning_resist)
                case 6: return elemDef(defender.earth_resist)
                case 7: return elemDef(defender.wind_resist)
                case 8: return elemDef(defender.other_resist)
                case _: return 1.0

        buffed_attack = atkPMVal() * buffVal(attacker.attack_level) * chargeVal()
        buffed_defense = defender.defense * buffVal(defender.defense_level) * guardVal()
        dmg = buffed_attack * (40/(40+buffed_defense)) * b_settings.getAtkConst() * formAtkVal() * formDefVal() * sevTypeVal() * elemResVal()

        return math.floor(dmg)

    def dodgeCalc():
        def buffVal(buff_val:int):
            if buff_val==1: return b_settings.getBuff1Mtp()
            elif buff_val==2: return b_settings.getBuff2Mtp()
            elif buff_val==3: return b_settings.getBuff3Mtp()
            elif buff_val==-1: return b_settings.getBuffn1Mtp()
            elif buff_val==-2: return b_settings.getBuffn2Mtp()
            elif buff_val==-3: return b_settings.getBuffn3Mtp()
            else: return 1.0

        atk_agi = attacker.agility * buffVal(attacker.agility_level)
        def_agi = defender.agility * buffVal(defender.agility_level)
        raw_probability = (atk_agi/def_agi) * b_settings.getDdgConst()
        dodge_num = random.uniform(0.0, 1.0)

        if(dodge_num<raw_probability): return True
        else: return False

    def critCalc():
        crit_probability = (attacker.luck/defender.luck) * b_settings.getCrtConst()
        crit_num = random.uniform(0.0, 1.0)

        if(crit_num<crit_probability): return True
        else: return False

    def elemRes():
        match element:
            case 0: return defender.slash_resist
            case 1: return defender.strike_resist
            case 2: return defender.pierce_resist
            case 3: return defender.fire_resist
            case 4: return defender.water_resist
            case 5: return defender.lightning_resist
            case 6: return defender.earth_resist
            case 7: return defender.wind_resist
            case 8: return defender.other_resist

    return [damageCalc(), dodgeCalc(), critCalc(), elemRes()]

def elementToString(element:int):
    match element:
        case 0: return "Slash"
        case 1: return "Strike"
        case 2: return "Pierce"
        case 3: return "Fire"
        case 4: return "Water"
        case 5: return "Lightning"
        case 6: return "Earth"
        case 7: return "Wind"
        case 8: return "Other-Type"

def severityToString(severity:int):
    match severity:
        case 1: return "light "
        case 2: return "medium "
        case 3: return "heavy "
        case 4: return "severe "
        case 5: return "colossal "
        case _: return " "

#ATTACK INTERACTIONS
def drainResAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int, dmg:int):
    s = ""
    defender.hp += dmg
    defender.mp += math.floor(defender.max_mp*b_settings.getNullMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " absorbs " + str(dmg) + " " + elementToString(element) + " damage from " + attacker.name + ". "
    return [attacker, defender, s]

def reflectResAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int, dmg:int):
    s = ""
    attacker.hp -= dmg
    defender.mp += math.floor(defender.max_mp*b_settings.getNullMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " reflects " + str(dmg) + " " + elementToString(element) + " damage to " + attacker.name + ". "
    return [attacker, defender, s]

def nullResAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int):
    s = ""
    defender.mp += math.floor(defender.max_mp*b_settings.getNullMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " blocks all " + elementToString(element) + " damage from " + attacker.name + ". "
    return [attacker, defender, s]

def dodgeAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings"):
    s = ""
    defender.mp += math.floor(defender.max_mp*b_settings.getDodgeMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " dodged the attack from " + attacker.name + ". "
    return [attacker, defender, s]

def weakResAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int, dmg:int, severity:int, atk_mp_gain:bool):
    s = ""
    defender.hp -= dmg
    if atk_mp_gain: attacker.mp += math.floor(attacker.max_mp*b_settings.getResMPGain())
    defender.mp += math.floor(defender.max_mp*b_settings.getWeakMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " takes " + str(dmg) + " weakness hitting " + severityToString(severity) + elementToString(element) + " damage from " + attacker.name + ". "
    return [attacker, defender, s]

def critAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int, dmg:int, severity:int, atk_mp_gain:bool):
    s = ""
    dmg *= 2
    defender.hp -= dmg
    if atk_mp_gain: attacker.mp += math.floor(attacker.max_mp*b_settings.getNorMPGain())
    defender.mp += math.floor(defender.max_mp*b_settings.getWeakMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " takes " + str(dmg) + " critical hitting " + severityToString(severity) + elementToString(element) + " damage from " + attacker.name + ". "
    return [attacker, defender, s]

def resResAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int, dmg:int, severity:int, atk_mp_gain:bool):
    s = ""
    defender.hp -= dmg
    if atk_mp_gain: attacker.mp += math.floor(attacker.max_mp*b_settings.getNorMPGain())
    defender.mp += math.floor(defender.max_mp*b_settings.getWeakMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " takes " + str(dmg) + " resistance-mitigated " + severityToString(severity) + elementToString(element) + " damage from " + attacker.name + ". "
    return [attacker, defender, s]

def norResAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", element:int, dmg:int, severity:int, atk_mp_gain:bool):
    s = ""
    defender.hp -= dmg
    if atk_mp_gain: attacker.mp += math.floor(attacker.max_mp*b_settings.getNorMPGain())
    defender.mp += math.floor(defender.max_mp*b_settings.getWeakMPGain())
    attacker.equalizeHpMp()
    defender.equalizeHpMp()
    s += defender.name + " takes " + str(dmg) + " " + severityToString(severity) + elementToString(element) + " damage from " + attacker.name + ". "
    return [attacker, defender, s]

#ATTACKS
def basicAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", pm_phys:bool, element:int):
    info = attackInfo(attacker, defender, b_settings, pm_phys, 0, element)
    dmg = info[0]
    does_dodge = info[1]
    does_crit = info[2]
    element_resistance = info[3]

    #0-Normal, 1-Weak, 2-Resists, 3-Null, 4-Reflect, 5-Drain

    if(element_resistance==5):
        battle_info = drainResAttack(attacker, defender, b_settings, element, dmg)
    elif(element_resistance==4):
        battle_info = reflectResAttack(attacker, defender, b_settings, element, dmg)
    elif(element_resistance==3):
        battle_info = nullResAttack(attacker, defender, b_settings, element)
    elif(does_dodge == True):
        battle_info = dodgeAttack(attacker, defender, b_settings)
    elif(element_resistance==1 and defender.guard==False):
        battle_info = weakResAttack(attacker, defender, b_settings, element, dmg, 0, True)
    elif(does_crit == True):
        battle_info = critAttack(attacker, defender, b_settings, element, dmg, 0, True)
    elif(element_resistance==2):
        battle_info = resResAttack(attacker, defender, b_settings, element, dmg, 0, True)
    else:
        battle_info = norResAttack(attacker, defender, b_settings, element, dmg, 0, True)

    return battle_info

def powerAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", pm_phys:bool, element:int, severity:int, mp_cost:int, force_hit:bool, force_dodge:bool):
    info = attackInfo(attacker, defender, b_settings, pm_phys, severity, element)
    dmg = info[0]
    does_dodge = info[1]
    does_crit = info[2]
    element_resistance = info[3]

    #Used for row attack
    if force_hit == True: does_dodge = False
    if force_dodge == True: does_dodge = True

    attacker.mp -= mp_cost

    #0-Normal, 1-Weak, 2-Resists, 3-Null, 4-Reflect, 5-Drain

    if(element_resistance==5):
        battle_info = drainResAttack(attacker, defender, b_settings, element, dmg)
    elif(element_resistance==4):
        battle_info = reflectResAttack(attacker, defender, b_settings, element, dmg)
    elif(element_resistance==3):
        battle_info = nullResAttack(attacker, defender, b_settings, element)
    elif(does_dodge == True):
        battle_info = dodgeAttack(attacker, defender, b_settings)
    elif(element_resistance==1 and defender.guard==False):
        battle_info = weakResAttack(attacker, defender, b_settings, element, dmg, severity, False)
    elif(does_crit == True):
        battle_info = critAttack(attacker, defender, b_settings, element, dmg, severity, False)
    elif(element_resistance==2):
        battle_info = resResAttack(attacker, defender, b_settings, element, dmg, severity, False)
    else:
        battle_info = norResAttack(attacker, defender, b_settings, element, dmg, severity, False)

    return battle_info

def attackAll(attacker:"Battler", defenders:list["Battler"], b_settings:"BattleSettings", pm_phys:bool, element:int, severity:int, mp_cost:int):
    attacker.mp -= mp_cost
    s = ""
    new_defenders = []

    for defender in defenders:
        temp_info = powerAttack(attacker, defender, b_settings, pm_phys, element, severity, 0, False, False)
        attacker = temp_info[0]
        new_defenders.append(temp_info[1])
        s += temp_info[2] + "\n"

    return [attacker, new_defenders, s]

def multiAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", pm_phys:bool, element:int, severity:int, attack_amount:int, mp_cost:int):
    info = attackInfo(attacker, defender, b_settings, pm_phys, severity, element)
    dmg = info[0]
    does_dodge = info[1]
    does_crit = info[2]
    element_resistance = info[3]

    attacker.mp -= mp_cost
    s = ""

    for i in range(attack_amount):
        if(element_resistance==5):
            battle_info = drainResAttack(attacker, defender, b_settings, element, dmg)
        elif(element_resistance==4):
            battle_info = reflectResAttack(attacker, defender, b_settings, element, dmg)
        elif(element_resistance==3):
            battle_info = nullResAttack(attacker, defender, b_settings, element)
        elif(does_dodge == True):
            battle_info = dodgeAttack(attacker, defender, b_settings)
        elif(element_resistance==1 and defender.guard==False):
            battle_info = weakResAttack(attacker, defender, b_settings, element, dmg, severity, False)
        elif(does_crit == True):
            battle_info = critAttack(attacker, defender, b_settings, element, dmg, severity, False)
        elif(element_resistance==2):
            battle_info = resResAttack(attacker, defender, b_settings, element, dmg, severity, False)
        else:
            battle_info = norResAttack(attacker, defender, b_settings, element, dmg, severity, False)

        attacker = battle_info[0]
        defender = battle_info[1]
        s += battle_info[2] + "\n"

    return [attacker, defender, s]

def drainAttack(attacker:"Battler", defender:"Battler", b_settings:"BattleSettings", pm_phys:bool, element:int, severity:int, mp_cost:int):
    info = attackInfo(attacker, defender, b_settings, pm_phys, severity, element)
    dmg = info[0]
    does_dodge = info[1]
    does_crit = info[2]
    element_resistance = info[3]

    attacker.mp -= mp_cost
    does_drain = False

    #0-Normal, 1-Weak, 2-Resists, 3-Null, 4-Reflect, 5-Drain

    if(element_resistance==5):
        battle_info = drainResAttack(attacker, defender, b_settings, element, dmg)
    elif(element_resistance==4):
        battle_info = reflectResAttack(attacker, defender, b_settings, element, dmg)
    elif(element_resistance==3):
        battle_info = nullResAttack(attacker, defender, b_settings, element)
    elif(does_dodge == True):
        battle_info = dodgeAttack(attacker, defender, b_settings)
    elif(element_resistance==1 and defender.guard==False):
        battle_info = weakResAttack(attacker, defender, b_settings, element, dmg, severity, False)
        does_drain = True
    elif(does_crit == True):
        battle_info = critAttack(attacker, defender, b_settings, element, dmg, severity, False)
        does_drain = True
    elif(element_resistance==2):
        battle_info = resResAttack(attacker, defender, b_settings, element, dmg, severity, False)
        does_drain = True
    else:
        battle_info = norResAttack(attacker, defender, b_settings, element, dmg, severity, False)
        does_drain = True

    if does_drain:
        battle_info[0].hp += dmg
        battle_info[0].equalizeHpMp()
        battle_info[2] += "\n" + attacker.name + " drains " + str(dmg) + " from " + defender.name + "."

    return battle_info

def splashAttack(attacker:"Battler", primary_defender_tag:str, defenders:list["Battler"], b_settings:"BattleSettings", pm_phys:bool, element:int, splash_element:int, severity:int, mp_cost:int):
    attacker.mp -= mp_cost
    s = ""
    new_defenders = []

    for defender in defenders:
        if defender.label == primary_defender_tag:
            temp_info = powerAttack(attacker, defender, b_settings, pm_phys, element, severity, 0, False, False)
        else:
            temp_info = basicAttack(attacker, defender, b_settings, False, splash_element)
        attacker = temp_info[0]
        new_defenders.append(temp_info[1])
        s += temp_info[2] + "\n"

    return [attacker, new_defenders, s]

def rowAttack(attacker:"Battler", defenders:list["Battler"], b_settings:"BattleSettings", pm_phys:bool, element:int, severity:int, fb_front:bool, mp_cost:int):
    attacker.mp -= mp_cost
    s = ""
    new_defenders = []

    for defender in defenders:
        if defender.formation == fb_front:
            temp_info = powerAttack(attacker, defender, b_settings, pm_phys, element, severity, 0, True, False)
        else:
            temp_info = powerAttack(attacker, defender, b_settings, pm_phys, element, severity, 0, False, True)
        attacker = temp_info[0]
        new_defenders.append(temp_info[1])
        s += temp_info[2] + "\n"

    return [attacker, new_defenders, s]