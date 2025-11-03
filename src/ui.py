import customtkinter as ctk
import webbrowser
from PIL import Image,ImageTk

appName = "Agenda App"
credits = "By Jordanocr"

# ====== Custom widgets =====
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
        ctk.set_default_color_theme("src/ui_theme/NightTrain.json")
        ctk.set_appearance_mode("dark")
        self.title(appName)
        self.geometry("400x400")
        self.resizable(False,False)
        try:
            self.iconbitmap("src/images/icon.ico")
        except Exception:
            icon_image = Image.open("src/images/icon.png")
            self.icon = ImageTk.PhotoImage(icon_image)
            self.iconphoto(True,self.icon)

        # ====== Image load setup ======
        image = Image.open("src/images/create.png")
        self.createAppointmentImage = ctk.CTkImage(image,size=(20,20))
        image = Image.open("src/images/edit.png")
        self.editAppointmentImage = ctk.CTkImage(image,size=(32,32))
        image = Image.open("src/images/export.png")
        self.exportBackupImage = ctk.CTkImage(image,size=(35,35))

        # ====== Widgets ======
        Blank(self)

        self.createAppointmentButton = ctk.CTkButton(self,font=("Arial",20),text="Create appointment",
                                                     width=200,height=40,corner_radius=30,image=self.createAppointmentImage,
                                                     border_width=1)
        self.createAppointmentButton.pack(pady=20)

        self.editAppointmentButton = ctk.CTkButton(self,font=("Arial",20),text="Edit appointments",
                                                   width=200,height=40,corner_radius=30,image=self.editAppointmentImage,
                                                   border_width=1)
        self.editAppointmentButton.pack(pady=20)

        self.exportBackupButton = ctk.CTkButton(self,font=("Arial",20),text="Export backup",
                                                width=240,height=40,corner_radius=30,image=self.exportBackupImage,
                                                border_width=1)
        self.exportBackupButton.pack(pady=20)

        self.githubLabel = ctk.CTkButton(self,font=("Arial",16),text=credits,
                                         width=140,height=28,corner_radius=30,fg_color="transparent",border_width=1,
                                         hover_color="#3b3b3b",command=self.openGithub)
        self.githubLabel.pack(pady=45)

    def openGithub(self):
        webbrowser.open("https://github.com/Jordanocr")

if __name__ == "__main__":
    MainMenu().mainloop()