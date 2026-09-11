import customtkinter as ctk
import battle_utils as bu
from tkinter import filedialog
from tkinter import messagebox
import csv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class ScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)      

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

        a_containers = []
        b_containers = []

        #Starting settings
        self.title("Custom RPG Calculator")
        self.iconbitmap("RPG Calculator Program/SunSymbol.ico")
        self.geometry("1920x1080")
        self.resizable(True, True)

        #Widget stretch config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=6)

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
                            for container in a_containers:
                                container.destroy() #Destroys container elements on canvas for new ones
                            for row in data_list:
                                #refactor data from data_list in battler classes
                                battler = bu.Battler(row)

                                #create list of buttons in a or b scrollframe
                                cnt = BattlerContainer(master=frame)
                                cnt.assignBattler(battler)

                                a_containers.append(cnt)
                        else:
                            for container in b_containers:
                                container.destroy() 
                            for row in data_list:
                                battler = bu.Battler(row)

                                cnt = BattlerContainer(master=frame)
                                cnt.assignBattler(battler)

                                b_containers.append(cnt)

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
        
        self.frame_a = ScrollFrame(master=self, corner_radius=1, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.frame_a.grid(row=1, column=0, padx=20, pady=20, sticky="nsew") #sticky="nsew" means the frame "sticks" to the 4 directions, north south east west

        self.frame_b = ScrollFrame(master=self, corner_radius=1, border_width=2, border_color="#e6f7ff", fg_color="#3a4b5c")
        self.frame_b.grid(row=1, column=1, padx=20, pady=20, sticky="nsew") 

        import_but_a = ctk.CTkButton(self, text="Import File for Team A", command=lambda: import_file(self.frame_a, True)) #command must be lambda wrapped to prevent it from executing on start
        import_but_a.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        import_but_b = ctk.CTkButton(self, text="Import File for Team B", command=lambda: import_file(self.frame_b, False)) 
        import_but_b.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        #Need to run the zoom after canvas finishes rendering
        self.after(100, lambda: app.state("zoomed"))


#This runs the app, always call it last. 
#__name__ = "__main__" makes sure this only runs if called directly from this file
if __name__ == "__main__":
    app = App()
    app.mainloop()