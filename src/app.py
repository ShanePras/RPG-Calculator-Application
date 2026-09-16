import customtkinter as ctk
import battle_utils as bu
from tkinter import filedialog
from tkinter import messagebox
import csv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

b_settings = bu.BattleSettings()

class ScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)      

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
        self.l_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[0]))
        self.l_atk_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.l_atk_entry)

        self.m_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Medium Attack Multiplier:")
        self.m_atk_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.m_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[1]))
        self.m_atk_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.m_atk_entry)

        self.h_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Heavy Attack Multiplier:")
        self.h_atk_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.h_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[2]))
        self.h_atk_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.h_atk_entry)

        self.s_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Severe Attack Multiplier:")
        self.s_atk_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.s_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[3]))
        self.s_atk_entry.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.s_atk_entry)

        self.c_atk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Colossal Attack Multiplier:")
        self.c_atk_label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.c_atk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[4]))
        self.c_atk_entry.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.c_atk_entry)

        self.res_wk_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Weak Multiplier:")
        self.res_wk_label.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        self.res_wk_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[5]))
        self.res_wk_entry.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.res_wk_entry)

        self.res_re_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Resist Multiplier:")
        self.res_re_label.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
        self.res_re_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[6]))
        self.res_re_entry.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.res_re_entry)

        self.bf_1_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level 1 Multiplier:")
        self.bf_1_label.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_1_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[7]))
        self.bf_1_entry.grid(row=7, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_1_entry)

        self.bf_2_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level 2 Multiplier:")
        self.bf_2_label.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_2_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[8]))
        self.bf_2_entry.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_2_entry)

        self.bf_3_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level 3 Multiplier:")
        self.bf_3_label.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_3_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[9]))
        self.bf_3_entry.grid(row=9, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_3_entry)

        self.bf_n1_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level -1 Multiplier:")
        self.bf_n1_label.grid(row=10, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_n1_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[10]))
        self.bf_n1_entry.grid(row=10, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_n1_entry)

        self.bf_n2_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level -2 Multiplier:")
        self.bf_n2_label.grid(row=11, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_n2_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[11]))
        self.bf_n2_entry.grid(row=11, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_n2_entry)

        self.bf_n3_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Buff Level -3 Multiplier:")
        self.bf_n3_label.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")
        self.bf_n3_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[12]))
        self.bf_n3_entry.grid(row=12, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.bf_n3_entry)

        self.form_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Backwards Formation Multiplier:")
        self.form_label.grid(row=13, column=0, padx=10, pady=10, sticky="nsew")
        self.form_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[13]))
        self.form_entry.grid(row=13, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.form_entry)

        self.charge_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Charge Multiplier:")
        self.charge_label.grid(row=14, column=0, padx=10, pady=10, sticky="nsew")
        self.charge_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[14]))
        self.charge_entry.grid(row=14, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.charge_entry)

        self.guard_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Guard Multiplier:")
        self.guard_label.grid(row=15, column=0, padx=10, pady=10, sticky="nsew")
        self.guard_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[15]))
        self.guard_entry.grid(row=15, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.guard_entry)

        self.atk_const_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Attack Constant:")
        self.atk_const_label.grid(row=16, column=0, padx=10, pady=10, sticky="nsew")
        self.atk_const_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[16]))
        self.atk_const_entry.grid(row=16, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.atk_const_entry)

        self.ddg_const_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Dodge Constant:")
        self.ddg_const_label.grid(row=17, column=0, padx=10, pady=10, sticky="nsew")
        self.ddg_const_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[17]))
        self.ddg_const_entry.grid(row=17, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.ddg_const_entry)

        self.crt_const_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Crit Chance Constant:")
        self.crt_const_label.grid(row=18, column=0, padx=10, pady=10, sticky="nsew")
        self.crt_const_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[18]))
        self.crt_const_entry.grid(row=18, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.crt_const_entry)

        self.heal_l_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Light Heal Multiplier:")
        self.heal_l_label.grid(row=19, column=0, padx=10, pady=10, sticky="nsew")
        self.heal_l_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[19]))
        self.heal_l_entry.grid(row=19, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.heal_l_entry)

        self.heal_m_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Medium Heal Multiplier:")
        self.heal_m_label.grid(row=20, column=0, padx=10, pady=10, sticky="nsew")
        self.heal_m_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[20]))
        self.heal_m_entry.grid(row=20, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.heal_m_entry)

        self.heal_h_label = ctk.CTkLabel(master=self.scroll_frame_1, text="Heavy Heal Multiplier:")
        self.heal_h_label.grid(row=21, column=0, padx=10, pady=10, sticky="nsew")
        self.heal_h_entry = ctk.CTkEntry(master=self.scroll_frame_1, placeholder_text=str(b_settings.set_lst[21]))
        self.heal_h_entry.grid(row=21, column=1, padx=10, pady=10, sticky="nsew")
        self.entries.append(self.heal_h_entry)

        def conf_changes(): 
                any_value_updated = False
                try:               
                    for i in range(22):
                        if self.entries[i].get() != "":
                            any_value_updated = True
                            b_settings.set_lst[i] = float(self.entries[i].get())
                    if any_value_updated:
                        messagebox.showinfo("Options Updated", "Values Successfully Updated!")
                except ValueError:
                    messagebox.showinfo("Error", "Invalid Type in an Entry. Please Input Only Float Values.")

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

        formation_string = "Position: "
        if(self.battler.formation): formation_string += "Front"
        else: formation_string += "Back"
        self.formation_label = ctk.CTkLabel(master=self, text=formation_string)
        self.formation_label.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        charge_string = ""
        if(self.battler.charge): charge_string += "Charged"
        else: charge_string += "Not Charged"
        self.charge_label = ctk.CTkLabel(master=self, text=charge_string)
        self.charge_label.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        guard_string = ""
        if(self.battler.guard): guard_string += "Guarding"
        else: guard_string += "Not Guarding"
        self.guard_label = ctk.CTkLabel(master=self, text=guard_string)
        self.guard_label.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        status_string = "Status: " + self.battler.status
        self.status_label = ctk.CTkLabel(master=self, text=status_string)
        self.status_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.a_containers = []
        self.b_containers = []

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
        self.columnconfigure(4, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=8)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.option_window = None

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
                            for container in self.a_containers:
                                container.destroy() #Destroys container elements on canvas for new ones
                            for row in data_list:
                                #refactor data from data_list in battler classes
                                battler = bu.Battler(row)

                                #create list of buttons in a or b scrollframe
                                cnt = BattlerContainer(master=frame)
                                cnt.assignBattler(battler)

                                #add buttons to a list so they can be sorted through
                                self.a_containers.append(cnt)

                                #Add labels to list to be added to options menu
                                label_list.append(battler.label)
                            self.battlers_a_menu.configure(values=label_list)
                        else:
                            self.battlers_b_menu.set("")
                            for container in self.b_containers:
                                container.destroy() 
                            for row in data_list:
                                battler = bu.Battler(row)

                                cnt = BattlerContainer(master=frame)
                                cnt.assignBattler(battler)

                                self.b_containers.append(cnt)

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
        
        self.option_button = ctk.CTkButton(master=self, corner_radius=5, text="Settings", command=lambda: open_settings())
        self.option_button.grid(row=0, column=4, padx=20, pady=20)
        
        self.frame_a = ctk.CTkScrollableFrame(master=self, corner_radius=5, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.frame_a.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew") #sticky="nsew" means the frame "sticks" to the 4 directions, north south east west

        self.frame_b = ctk.CTkScrollableFrame(master=self, corner_radius=5, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.frame_b.grid(row=2, column=2, columnspan=2, padx=20, pady=20, sticky="nsew") 

        self.import_but_a = ctk.CTkButton(self, text="Import File for Team A", command=lambda: import_file(self.frame_a, True)) #command must be lambda wrapped to prevent it from executing on start
        self.import_but_a.grid(row=1, column=0, padx=20, pady=20, sticky="n")

        self.import_but_b = ctk.CTkButton(self, text="Import File for Team B", command=lambda: import_file(self.frame_b, False)) 
        self.import_but_b.grid(row=1, column=2, padx=20, pady=20, sticky="n")

        self.sw_label = ctk.CTkLabel(master=self, text="Selected Attacking Team")
        self.sw_label.grid(row=3, column=1, padx=20, pady=20, sticky="e")

        self.is_b = ctk.StringVar(value="Team A")
        self.team_sw = ctk.CTkSwitch(master=self, text="Team A", command=lambda: a_b_switch(), variable=self.is_b, onvalue="Team B", offvalue="Team A")
        self.team_sw.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.names_a_lbl = ctk.CTkLabel(master=self, text="Team A - Selected Fighter:")
        self.names_a_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.battlers_a_menu = ctk.CTkOptionMenu(master=self, values=[])
        self.battlers_a_menu.set("")
        self.battlers_a_menu.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.names_b_lbl = ctk.CTkLabel(master=self, text="Team B - Selected Fighter:")
        self.names_b_lbl.grid(row=4, column=2, padx=10, pady=10, sticky="e")

        self.battlers_b_menu = ctk.CTkOptionMenu(master=self, values=[])
        self.battlers_b_menu.set("")
        self.battlers_b_menu.grid(row=4, column=3, padx=10, pady=10, sticky="w")


#This runs the app, always call it last. 
#__name__ = "__main__" makes sure this only runs if called directly from this file
if __name__ == "__main__":
    app = App()
    app.mainloop()