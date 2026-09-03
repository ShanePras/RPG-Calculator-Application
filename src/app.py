import customtkinter as ctk
import battle_utils as bu
from tkinter import filedialog
import csv

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class ScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        a_battlers = []
        b_battlers = []
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
                            for i in range(0,18):
                                if i<2:
                                    new_row.append(row[i])
                                else:
                                    new_row.append(int(row[i]))
                            data_list.append(new_row)
                        if(is_a): 
                            a_battlers = [] #Importing new data, so we clear the old data
                            for container in a_containers:
                                container.destroy() #Destroys container elements on canvas for new ones
                            for row in data_list:
                                #refactor data from data_list in battler classes
                                battler = bu.Battler(row)

                                #create list of buttons in a or b scrollframe
                                cnt = ctk.CTkFrame(master=frame)
                                cnt.pack(pady=10, padx=10, fill="both", expand=True)

                                cnt_lbl = ctk.CTkLabel(master=cnt, text=battler.name)
                                cnt_lbl.pack(pady=10)

                                a_containers.append(cnt)
                                a_battlers.append(battler)
                        else:
                            b_battlers = [] #Importing new data, so we clear the old data
                            for container in b_containers:
                                container.destroy() #Destroys container elements on canvas for new ones
                            for row in data_list:
                                #refactor data from data_list in battler classes
                                battler = bu.Battler(row)

                                #create list of buttons in a or b scrollframe
                                cnt = ctk.CTkFrame(master=frame)
                                cnt.pack(pady=10, padx=10, fill="both", expand=True)

                                cnt_lbl = ctk.CTkLabel(master=cnt, text=battler.name)
                                cnt_lbl.pack(pady=10)

                                b_containers.append(cnt)
                                b_battlers.append(battler)

                except SyntaxError:
                    print("Error: CSV File is incorrectly formated.")
                except ValueError:
                    print("Error: Bad type in CSV file. Please reformat.")
                except IndexError:
                    print("Error: CSV file is missing data.")
                finally:
                    f.close()

            else:
                print("No file selected")
        
        self.frame_a = ScrollFrame(master=self, corner_radius=0, fg_color="transparent")
        self.frame_a.grid(row=1, column=0, padx=20, pady=20, sticky="nsew") #sticky="nsew" means the frame "sticks" to the 4 directions, north south east west

        self.frame_b = ScrollFrame(master=self, corner_radius=0, fg_color="transparent")
        self.frame_b.grid(row=1, column=1, padx=20, pady=20, sticky="nsew") 

        import_but_a = ctk.CTkButton(self, text="Import File for Team A", command=lambda: import_file(self.frame_a, True)) #command must be lambda wrapped to prevent it from executing on start
        import_but_a.grid(row=0, column=0, padx=20, pady=20, sticky="")

        import_but_b = ctk.CTkButton(self, text="Import File for Team B", command=lambda: import_file(self.frame_b, False)) 
        import_but_b.grid(row=0, column=1, padx=20, pady=20, sticky="")

        #Need to run the zoom after canvas finishes rendering
        self.after(100, lambda: app.state("zoomed"))


#This runs the app, always call it last. 
#__name__ = "__main__" makes sure this only runs if called directly from this file
if __name__ == "__main__":
    app = App()
    app.mainloop()