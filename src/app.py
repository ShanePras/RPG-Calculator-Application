import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Starting settings
        self.title("Custom RPG Calculator")
        self.iconbitmap("RPG Calculator Program/SunSymbol.ico")
        self.geometry("800x600")
        self.resizable(True, True)
        #Need to run the zoom after canvas finishes rendering
        self.after(100, lambda: app.state("zoomed"))


#This runs the app, always call it last
app = App()
app.mainloop()