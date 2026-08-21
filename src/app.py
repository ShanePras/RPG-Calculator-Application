import customtkinter as ctk
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

        #Starting settings
        self.title("Custom RPG Calculator")
        self.iconbitmap("RPG Calculator Program/SunSymbol.ico")
        self.geometry("1920x1080")
        self.resizable(True, True)

        #Widget stretch config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        def import_file():
            file_path = filedialog.askopenfilename(
                title="Import CSV",
                filetypes=[("CSV files", "*.csv")]
            )

            if file_path:
                print("Selected file:", file_path)
            else:
                print("Bad file error")

        import_but_a = ctk.CTkButton(self, text="Import File for Team A", command=lambda: import_file()) #command must be lambda wrapped to prevent it from executing on start
        import_but_a.grid(row=0, column=0, padx=20, pady=20, sticky="")

        import_but_b = ctk.CTkButton(self, text="Import File for Team B", command=lambda: import_file()) #command must be lambda wrapped to prevent it from executing on start
        import_but_b.grid(row=0, column=1, padx=20, pady=20, sticky="")
        
        self.frame_a = ScrollFrame(master=self, corner_radius=0, fg_color="transparent")
        self.frame_a.grid(row=1, column=0, padx=20, pady=20, sticky="nsew") #sticky="nsew" means the frame "sticks" to the 4 directions, north south east west

        self.frame_b = ScrollFrame(master=self, corner_radius=0, fg_color="transparent")
        self.frame_b.grid(row=1, column=1, padx=20, pady=20, sticky="nsew") 

        #Need to run the zoom after canvas finishes rendering
        self.after(100, lambda: app.state("zoomed"))


#This runs the app, always call it last. Also, __name__ = "__main__" makes sure this only runs if called directly from this file
if __name__ == "__main__":
    app = App()
    app.mainloop()