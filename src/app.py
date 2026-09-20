import customtkinter as ctk
import battle_utils as bu
from tkinter import filedialog
from tkinter import messagebox
import csv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

b_settings = bu.BattleSettings()    

class OptionWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title("RPG Calculator Settings")
        self.geometry("1280x720")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.after(100, self.focus)

        self.entries = []

        self.scroll_frame_1 = ctk.CTkScrollableFrame(master=self)
        self.scroll_frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.conf_change_btn = ctk.CTkButton(master=self, corner_radius=5, text="Confirm Changes", command=lambda: conf_changes())
        self.conf_change_btn.grid(row=1, column=0, padx=20, pady=20, sticky="ns")

        self.l_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Light Attack Multiplier:")
        self.l_atk_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.l_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getLAtkMtp()))
        self.l_atk_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.l_atk_entry)

        self.m_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Medium Attack Multiplier:")
        self.m_atk_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.m_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getMAtkMtp()))
        self.m_atk_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.m_atk_entry)

        self.h_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Heavy Attack Multiplier:")
        self.h_atk_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.h_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getHAtkMtp()))
        self.h_atk_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.h_atk_entry)

        self.s_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Severe Attack Multiplier:")
        self.s_atk_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.s_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getSAtkMtp()))
        self.s_atk_entry.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.s_atk_entry)

        self.c_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Colossal Attack Multiplier:")
        self.c_atk_label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.c_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getCAtkMtp()))
        self.c_atk_entry.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.c_atk_entry)

        self.res_wk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Weak Multiplier:")
        self.res_wk_label.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        self.res_wk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getWeakMtp()))
        self.res_wk_entry.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.res_wk_entry)

        self.res_re_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Resist Multiplier:")
        self.res_re_label.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
        self.res_re_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getResMtp()))
        self.res_re_entry.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.res_re_entry)

        self.bf_1_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level 1 Multiplier:")
        self.bf_1_label.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_1_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getBuff1Mtp()))
        self.bf_1_entry.grid(row=7, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_1_entry)

        self.bf_2_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level 2 Multiplier:")
        self.bf_2_label.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_2_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getBuff2Mtp()))
        self.bf_2_entry.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_2_entry)

        self.bf_3_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level 3 Multiplier:")
        self.bf_3_label.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_3_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getBuff3Mtp()))
        self.bf_3_entry.grid(row=9, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_3_entry)

        self.bf_n1_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level -1 Multiplier:")
        self.bf_n1_label.grid(row=10, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_n1_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getBuffn1Mtp()))
        self.bf_n1_entry.grid(row=10, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_n1_entry)

        self.bf_n2_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level -2 Multiplier:")
        self.bf_n2_label.grid(row=11, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_n2_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getBuffn2Mtp()))
        self.bf_n2_entry.grid(row=11, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_n2_entry)

        self.bf_n3_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level -3 Multiplier:")
        self.bf_n3_label.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_n3_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getBuffn3Mtp()))
        self.bf_n3_entry.grid(row=12, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_n3_entry)

        self.form_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Backwards Formation Multiplier:")
        self.form_label.grid(row=13, column=0, padx=10, pady=10, sticky="nsew")
        self.form_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getFormMtp()))
        self.form_entry.grid(row=13, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.form_entry)

        self.charge_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Charge Multiplier:")
        self.charge_label.grid(row=14, column=0, padx=10, pady=10, sticky="nsew")
        self.charge_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getChargeMtp()))
        self.charge_entry.grid(row=14, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.charge_entry)

        self.guard_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Guard Multiplier:")
        self.guard_label.grid(row=15, column=0, padx=10, pady=10, sticky="nsew")
        self.guard_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getGuardMtp()))
        self.guard_entry.grid(row=15, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.guard_entry)

        self.atk_const_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Attack Constant:")
        self.atk_const_label.grid(row=16, column=0, padx=10, pady=10, sticky="nsew")
        self.atk_const_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getAtkConst()))
        self.atk_const_entry.grid(row=16, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.atk_const_entry)

        self.ddg_const_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Dodge Constant:")
        self.ddg_const_label.grid(row=17, column=0, padx=10, pady=10, sticky="nsew")
        self.ddg_const_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getDdgConst()))
        self.ddg_const_entry.grid(row=17, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.ddg_const_entry)

        self.crt_const_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Crit Chance Constant:")
        self.crt_const_label.grid(row=18, column=0, padx=10, pady=10, sticky="nsew")
        self.crt_const_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getCrtConst()))
        self.crt_const_entry.grid(row=18, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.crt_const_entry)

        self.heal_l_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Light Heal Multiplier:")
        self.heal_l_label.grid(row=19, column=0, padx=10, pady=10, sticky="nsew")
        self.heal_l_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getLHealMtp()))
        self.heal_l_entry.grid(row=19, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.heal_l_entry)

        self.heal_m_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Medium Heal Multiplier:")
        self.heal_m_label.grid(row=20, column=0, padx=10, pady=10, sticky="nsew")
        self.heal_m_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getMHealMtp()))
        self.heal_m_entry.grid(row=20, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.heal_m_entry)

        self.heal_h_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Heavy Heal Multiplier:")
        self.heal_h_label.grid(row=21, column=0, padx=10, pady=10, sticky="nsew")
        self.heal_h_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getHHealMtp()))
        self.heal_h_entry.grid(row=21, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.heal_h_entry)

        self.l_atk_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Light Attack MP:")
        self.l_atk_mp_label.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.l_atk_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getLAtkMp()))
        self.l_atk_mp_entry.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.l_atk_mp_entry)

        self.m_atk_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Medium Attack MP:")
        self.m_atk_mp_label.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.m_atk_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getMAtkMp()))
        self.m_atk_mp_entry.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.m_atk_mp_entry)

        self.h_atk_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Heavy Attack MP:")
        self.h_atk_mp_label.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.h_atk_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getHAtkMp()))
        self.h_atk_mp_entry.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.h_atk_mp_entry)

        self.s_atk_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Severe Attack MP:")
        self.s_atk_mp_label.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
        self.s_atk_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getSAtkMp()))
        self.s_atk_mp_entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.s_atk_mp_entry)

        self.c_atk_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Colossal Attack MP:")
        self.c_atk_mp_label.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
        self.c_atk_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getCAtkMp()))
        self.c_atk_mp_entry.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.c_atk_mp_entry)

        self.atk_all_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Attack All MP Increase:")
        self.atk_all_mp_label.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")
        self.atk_all_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getAtkAllMpAdd()))
        self.atk_all_mp_entry.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.atk_all_mp_entry)

        self.multi_atk_mp_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Multi Attack MP Increase:")
        self.multi_atk_mp_label.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")
        self.multi_atk_mp_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getMultiattackMpAdd()))
        self.multi_atk_mp_entry.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.multi_atk_mp_entry)

        self.nor_mp_gain_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Normal MP Gain Percentage:")
        self.nor_mp_gain_label.grid(row=7, column=2, padx=10, pady=10, sticky="nsew")
        self.nor_mp_gain_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getNorMPGain()))
        self.nor_mp_gain_entry.grid(row=7, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.nor_mp_gain_entry)

        self.res_mp_gain_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Resist MP Gain Percentage:")
        self.res_mp_gain_label.grid(row=8, column=2, padx=10, pady=10, sticky="nsew")
        self.res_mp_gain_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getResMPGain()))
        self.res_mp_gain_entry.grid(row=8, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.res_mp_gain_entry)

        self.wk_mp_gain_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Weak MP Gain Percentage:")
        self.wk_mp_gain_label.grid(row=9, column=2, padx=10, pady=10, sticky="nsew")
        self.wk_mp_gain_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getWeakMPGain()))
        self.wk_mp_gain_entry.grid(row=9, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.wk_mp_gain_entry)

        self.nu_mp_gain_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Null MP Gain Percentage:")
        self.nu_mp_gain_label.grid(row=10, column=2, padx=10, pady=10, sticky="nsew")
        self.nu_mp_gain_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getNullMPGain()))
        self.nu_mp_gain_entry.grid(row=10, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.nu_mp_gain_entry)

        self.ddg_mp_gain_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Dodge MP Gain Percentage:")
        self.ddg_mp_gain_label.grid(row=11, column=2, padx=10, pady=10, sticky="nsew")
        self.ddg_mp_gain_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.getDodgeMPGain()))
        self.ddg_mp_gain_entry.grid(row=11, column=3, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.ddg_mp_gain_entry)

        def conf_changes(): 
            any_value_updated = False
            try:               
                for i in range(22):
                    if self.entries[i].get() != "":
                        any_value_updated = True
                        b_settings.set_lst[i] = float(self.entries[i].get())
                for i in range(22, 34):
                    if self.entries[i].get() != "":
                        any_value_updated = True
                        b_settings.mp_lst[i-22] = float(self.entries[i].get())
                if any_value_updated:
                    messagebox.showinfo("Options Updated", "Values Successfully Updated!")
            except ValueError:
                messagebox.showinfo("Error", "Invalid Type in an Entry. Please Input Only Float Values.")
            finally:
                self.destroy()

class BattlerContainer(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def assignBattler(self, _battler:bu.Battler):
        #This method should be called immediately after init. It just has a seperate method because constructor parameters cant take both battler and master
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.battler = _battler

        #add hp, mp, atk lvl, def lvl, agi lvl, front/back status, guard status, charge status

        self.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.name_lbl = ctk.CTkLabel(master=self, text=self.battler.name)
        self.name_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        hp_string = "HP: " + str(self.battler.hp) + "/" + str(self.battler.max_hp)
        self.hp_label = ctk.CTkLabel(master=self, text=hp_string)
        self.hp_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        mp_string = "MP: " + str(self.battler.mp) + "/" + str(self.battler.max_mp)
        self.mp_label = ctk.CTkLabel(master=self, text=mp_string)
        self.mp_label.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        atk_lvl_string = "ATK LVL: " + str(self.battler.attack_level)
        self.atk_lvl_label = ctk.CTkLabel(master=self, text=atk_lvl_string)
        self.atk_lvl_label.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        def_lvl_string = "DEF LVL: " + str(self.battler.defense_level)
        self.def_lvl_label = ctk.CTkLabel(master=self, text=def_lvl_string)
        self.def_lvl_label.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

        agi_lvl_string = "AGI LVL: " + str(self.battler.agility_level)
        self.agi_lvl_label = ctk.CTkLabel(master=self, text=agi_lvl_string)
        self.agi_lvl_label.grid(row=0, column=5, padx=10, pady=10, sticky="nsew")

        def form_switch():
            if self.formation_var.get():
                self.formation_switch.configure(text="Position: Back")
            else:
                self.formation_switch.configure(text="Position: Front")
        self.formation_var = ctk.BooleanVar(value=False)
        self.formation_switch = ctk.CTkSwitch(master=self, text="Position: Front", command=lambda: form_switch(), variable=self.formation_var, onvalue=True, offvalue=False)
        self.formation_switch.grid(row=1, column=1, padx=10, pady=10, sticky="ns")

        def guard_switch():
            if self.guard_var.get():
                self.guard_switch.configure(text="  Is Guarding  ")
            else:
                self.guard_switch.configure(text="Not Guarding")
        self.guard_var = ctk.BooleanVar(value=False)
        self.guard_switch = ctk.CTkSwitch(master=self, text="Not Guarding", command=lambda: guard_switch(), variable=self.guard_var, onvalue=True, offvalue=False)
        self.guard_switch.grid(row=1, column=2, padx=10, pady=10, sticky="ns")

        charge_string = ""
        if(self.battler.charge): charge_string += "Charged"
        else: charge_string += "Not Charged"
        self.charge_label = ctk.CTkLabel(master=self, text=charge_string)
        self.charge_label.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        status_string = "Status: " + self.battler.status
        self.status_label = ctk.CTkLabel(master=self, text=status_string)
        self.status_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

class AttackWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title("Attack Menu")
        self.geometry("1280x720")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        self.after(100, self.focus)

        def perform_attack():
            def phys_magic_bool():
                if self.pm_menu.get() == "Physical": return True
                else: return False

            def elem_int():
                match self.ele_menu.get():
                    case "Slash": return 0
                    case "Strike": return 1
                    case "Pierce": return 2
                    case "Fire": return 3
                    case "Water": return 4
                    case "Lightning": return 5
                    case "Earth": return 6
                    case "Wind": return 7
                    case "Other": return 8
                    case _: 
                        print("Type Error in elem_int()")
                        return 0

            if self.type_menu_var.get() == "Attack":
                if master.is_b.get() == "Team A":
                    attacker = master.findBattler(master.battlers_a_menu.get(), True)
                    defender = master.findBattler(master.battlers_b_menu.get(), False)
                else:
                    attacker = master.findBattler(master.battlers_b_menu.get(), False)
                    defender = master.findBattler(master.battlers_a_menu.get(), True)

                battle_info = bu.basicAttack(attacker, defender, b_settings, phys_magic_bool(), elem_int())

                master.log_console.configure(text=battle_info[2])

                if master.is_b.get() == "Team A":
                    master.changeBattlerInfo(master.battlers_a_menu.get(), True, battle_info[0])
                    master.changeBattlerInfo(master.battlers_b_menu.get(), False, battle_info[1])
                else:
                    master.changeBattlerInfo(master.battlers_b_menu.get(), False, battle_info[0])
                    master.changeBattlerInfo(master.battlers_a_menu.get(), True, battle_info[1])

                self.destroy()

        self.type_lbl = ctk.CTkLabel(master=self, text="Attack Type:")
        self.type_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        def type_menu_callback(choice:str):
            print(choice)
            #this will change the rest of the render depending on choice
        self.type_menu_var = ctk.StringVar(value="Attack")
        self.type_menu = ctk.CTkOptionMenu(master=self, values=["Attack", "Power Attack", "Multi Attack", "Drain Attack", "Row Attack", "Splash Attack"], command=type_menu_callback, variable=self.type_menu_var)
        self.type_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.pm_lbl = ctk.CTkLabel(master=self, text="Physical or Ranged:")
        self.pm_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.pm_menu = ctk.CTkOptionMenu(master=self, values=["Physical", "Ranged"])
        self.pm_menu.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.ele_lbl = ctk.CTkLabel(master=self, text="Element:")
        self.ele_lbl.grid(row=0, column=4, padx=10, pady=10, sticky="e")

        self.ele_menu = ctk.CTkOptionMenu(master=self, values=["Slash", "Strike", "Pierce", "Fire", "Water", "Lightning", "Earth", "Wind", "Other"])
        self.ele_menu.grid(row=0, column=5, padx=10, pady=10, sticky="w")

        self.mp_cost_lbl = ctk.CTkLabel(master=self, text="MP Cost: 0")
        self.mp_cost_lbl.grid(row=2, column=1, padx=10, pady=10, sticky="s")

        self.atk_btn = ctk.CTkButton(master=self, text="Confirm", command=perform_attack)
        self.atk_btn.grid(row=2, column=3, padx=10, pady=10, sticky="s")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.a_container = []
        self.b_container = []

        #Starting settings
        self.title("Custom RPG Calculator")
        self.iconbitmap("RPG Calculator Program/SunSymbol.ico")
        self.geometry("1920x1080")
        self.resizable(True, True)

        #Widget stretch config
        self.columnconfigure(0, weight=15)
        self.columnconfigure(1, weight=15)
        self.columnconfigure(2, weight=15)
        self.columnconfigure(3, weight=15)
        self.columnconfigure(4, weight=15)
        self.columnconfigure(5, weight=15)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=16)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=4)
        self.rowconfigure(6, weight=8)

        self.option_window = None
        self.attack_window = None

        #Need to run the zoom after canvas finishes rendering
        self.after(100, lambda: app.state("zoomed"))

        def a_b_switch():
            self.team_sw.configure(text=self.is_b.get())

        def show_msg(title:str, msg:str):
            messagebox.showinfo(title, msg)

        def import_file(frame, is_a=True):
            file_path = filedialog.askopenfilename(
                title="Import CSV",
                filetypes=[("CSV files", "*.csv")]
            )

            if file_path:
                try:
                    data_list = []
                    label_list = [] #Name tag list used to manage options menus
                    with open(file_path, "r") as f:
                        data = csv.reader(f)
                        for row in data:
                            new_row=[]
                            for i in range(0,19):
                                if i<2:
                                    new_row.append(row[i])
                                else:
                                    new_row.append(int(row[i]))
                            data_list.append(new_row)
                        if(is_a): 
                            self.battlers_a_menu.set("")
                            for container in self.a_container:
                                container.destroy() #Destroys container elements on canvas for new ones
                            for row in data_list:
                                #refactor data from data_list in battler classes
                                battler = bu.Battler(row)

                                #create list of buttons in a or b scrollframe
                                cnt = BattlerContainer(master=frame)
                                cnt.assignBattler(battler)

                                #add buttons to a list so they can be sorted through
                                self.a_container.append(cnt)

                                #Add labels to list to be added to options menu
                                label_list.append(battler.label)
                            self.battlers_a_menu.configure(values=label_list)
                        else:
                            self.battlers_b_menu.set("")
                            for container in self.b_container:
                                container.destroy() 
                            for row in data_list:
                                battler = bu.Battler(row)

                                cnt = BattlerContainer(master=frame)
                                cnt.assignBattler(battler)

                                self.b_container.append(cnt)

                                label_list.append(battler.label)
                            self.battlers_b_menu.configure(values=label_list)

                except SyntaxError:
                    show_msg("Error", "Error: CSV File is incorrectly formated.")
                except ValueError:
                    show_msg("Error", "Error: Bad type in CSV file. Please reformat.")
                except IndexError:
                    show_msg("Error", "Error: CSV file is missing data.")
                finally:
                    f.close()

            else:
                show_msg("Error", "No file selected.")

        def open_settings():
            if self.option_window is None or not self.option_window.winfo_exists():
                self.option_window = OptionWindow(master=self)
            else:
                self.option_window.focus()

        def attack_menu():
            if self.battlers_a_menu.get() != "" and self.battlers_b_menu.get() != "":
                if self.attack_window is None or not self.attack_window.winfo_exists():
                    self.attack_window = AttackWindow(master=self)
                else:
                    self.attack_window.focus()
            else:
                show_msg("Error", "Please select fighters in the A and B dropdown before pressing a command.")

        def heal_menu():
            pass

        def buff_menu():
            pass

        def charge():
            pass

        def scan():
            pass

        def status_menu():
            pass
        
        self.option_button = ctk.CTkButton(master=self, corner_radius=5, text="Settings", command=lambda: open_settings())
        self.option_button.grid(row=0, column=6, padx=20, pady=20)
        
        self.frame_a = ctk.CTkScrollableFrame(master=self, corner_radius=5, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.frame_a.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="nsew") #sticky="nsew" means the frame "sticks" to the 4 directions, north south east west

        self.frame_b = ctk.CTkScrollableFrame(master=self, corner_radius=5, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.frame_b.grid(row=2, column=3, columnspan=3, padx=20, pady=20, sticky="nsew") 

        self.import_but_a = ctk.CTkButton(self, text="Import File for Team A", command=lambda: import_file(self.frame_a, True)) #command must be lambda wrapped to prevent it from executing on start
        self.import_but_a.grid(row=1, column=1, padx=20, pady=20, sticky="n")

        self.import_but_b = ctk.CTkButton(self, text="Import File for Team B", command=lambda: import_file(self.frame_b, False)) 
        self.import_but_b.grid(row=1, column=4, padx=20, pady=20, sticky="n")

        self.sw_label = ctk.CTkLabel(master=self, text="Selected Attacking Team")
        self.sw_label.grid(row=3, column=2, padx=20, pady=20, sticky="e")

        self.is_b = ctk.StringVar(value="Team A")
        self.team_sw = ctk.CTkSwitch(master=self, text="Team A", command=lambda: a_b_switch(), variable=self.is_b, onvalue="Team B", offvalue="Team A")
        self.team_sw.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        self.names_a_lbl = ctk.CTkLabel(master=self, text="Team A - Selected Fighter:")
        self.names_a_lbl.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="e")

        self.battlers_a_menu = ctk.CTkOptionMenu(master=self, values=[])
        self.battlers_a_menu.set("")
        self.battlers_a_menu.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.names_b_lbl = ctk.CTkLabel(master=self, text="Team B - Selected Fighter:")
        self.names_b_lbl.grid(row=4, column=3, padx=10, pady=10, sticky="e")

        self.battlers_b_menu = ctk.CTkOptionMenu(master=self, values=[])
        self.battlers_b_menu.set("")
        self.battlers_b_menu.grid(row=4, column=4, columnspan=2, padx=10, pady=10, sticky="w")

        self.atk_button = ctk.CTkButton(master=self, text="Attack", command=lambda: attack_menu())
        self.atk_button.grid(row=5, column=0, padx=20, pady=20, sticky="nsew")

        self.heal_button = ctk.CTkButton(master=self, text="Heal", command=lambda: heal_menu())
        self.heal_button.grid(row=5, column=1, padx=20, pady=20, sticky="nsew")

        self.buff_button = ctk.CTkButton(master=self, text="Buff/Debuff", command=lambda: buff_menu())
        self.buff_button.grid(row=5, column=2, padx=20, pady=20, sticky="nsew")

        self.charge_button = ctk.CTkButton(master=self, text="Charge", command=lambda: charge())
        self.charge_button.grid(row=5, column=3, padx=20, pady=20, sticky="nsew")

        self.scan_button = ctk.CTkButton(master=self, text="Scan", command=lambda: scan())
        self.scan_button.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")

        self.status_button = ctk.CTkButton(master=self, text="Inflict Status", command=lambda: status_menu())
        self.status_button.grid(row=5, column=5, padx=20, pady=20, sticky="nsew")

        self.log_console = ctk.CTkLabel(master=self, text="", corner_radius=10, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.log_console.grid(row=6, column=2, columnspan=5, padx=20, pady=20, sticky="nsew")

    def findBattler(self, tag:str, is_a:bool):
        if is_a:
            for cont in self.a_container:
                if cont.battler.label == tag:
                    return cont.battler
        else:
            for cont in self.b_container:
                if cont.battler.label == tag:
                    return cont.battler

    def changeBattlerInfo(self, tag:str, is_a:bool, new_battler:"bu.Battler"):
        if is_a:
            for cont in self.a_container:
                if cont.battler.label == tag:
                    cont.assignBattler(new_battler)
        else:
            for cont in self.b_container:
                if cont.battler.label == tag:
                    cont.assignBattler(new_battler)

#This runs the app, always call it last. 
#__name__ = "__main__" makes sure this only runs if called directly from this file
if __name__ == "__main__":
    app = App()
    app.mainloop()