import customtkinter as ctk

appName = "Agenda"
theme = ""

# ====== Custom widgets =====
class Label(ctk.CTk):
    """ A pre-configured themed label widget. """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        """ Just configure based on my chosen theme colors! """

class Blank(ctk.CTkLabel):
    """ A basic blank space widget ready to use. """
    def __init__(self,parent,py=0,px=0):
        super().__init__(parent,text="")
        self.pack(pady=py,padx=px)

# ====== UI screens ======
class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ====== Inicial settings ======
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")
        self.title(appName)
        self.geometry("600x400")

        # ====== Widgets ======
        Blank(self)

        self.titleLabel = ctk.CTkLabel(self,font=("Arial",18),text=appName)
        self.titleLabel.pack()

        Blank(self)

if __name__ == "__main__":
    MainMenu().mainloop()
