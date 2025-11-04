import customtkinter as ctk
import webbrowser,logic
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
    """ Main menu interface. """
    def __init__(self):
        super().__init__()

        # ====== Inicial settings ======
        ctk.set_default_color_theme("src/ui_theme/NightTrain.json")
        ctk.set_appearance_mode("dark")
        self.title(appName)
        self.geometry("400x400")
        self.resizable(False,False)
        self.configure(fg_color="#030515")

        # ====== Cross-platform window icon ======
        try:
            # Windows requires .ico.
            self.iconbitmap("src/images/icon.ico")
        except Exception:
            # Linux and MacOS requires png.
            icon_image = Image.open("src/images/icon.png")
            self.icon_photo = ImageTk.PhotoImage(icon_image)
            # Slight delay so the window manager recognizes it.
            self.after(100, lambda: self.iconphoto(True, self.icon_photo))

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
                                                     border_width=1,command=self.openCreateAppointment)
        self.createAppointmentButton.pack(pady=20)

        self.editAppointmentButton = ctk.CTkButton(self,font=("Arial",20),text="Edit appointments",
                                                   width=200,height=40,corner_radius=30,image=self.editAppointmentImage,
                                                   border_width=1,command=self.openEditAppointment)
        self.editAppointmentButton.pack(pady=20)

        self.exportBackupButton = ctk.CTkButton(self,font=("Arial",20),text="Export backup",
                                                width=240,height=40,corner_radius=30,image=self.exportBackupImage,
                                                border_width=1)
        self.exportBackupButton.pack(pady=20)

        self.githubLabel = ctk.CTkButton(self,font=("Arial",16),text=credits,
                                         width=140,height=28,corner_radius=30,fg_color="transparent",border_width=1,
                                         hover_color="#3b3b3b",command=self.openGithub)
        self.githubLabel.pack(pady=45)

    # ====== Methods & Commands ======
    def openCreateAppointment(self):
        """ Opens the create appointment interface and hides the main menu. """
        self.withdraw()
        CreateAppointment(self)

    def openEditAppointment(self):
        """ Opens the edit appointment interface and hides the main menu. """
        self.withdraw()
        EditAppointment(self)

    def openGithub(self):
        """ Opens the default browser and navigates to my GitHub profile. """
        webbrowser.open("https://github.com/Jordanocr")

class CreateAppointment(ctk.CTkToplevel):
    """ Create appointment interface. """
    def __init__(self,parent,edit=False):
        super().__init__(parent)

        # ====== Inicial settings ======
        self.title("Create appointment")
        self.geometry("700x700")
        self.parent = parent
        self.edit = edit

        # ====== Widgets ======
        self.titleLabel = ctk.CTkLabel(self,font=("Arial",40),text="Create appointment")
        self.titleLabel.pack(pady=10)

        Blank(self,py=10)

        self.nameEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Name:",width=300,height=30,corner_radius=30)
        self.nameEntry.pack(pady=10)

        self.descriptionLabel = ctk.CTkLabel(self,font=("Arial",18),text="Description:")
        self.descriptionLabel.pack(pady=5)

        self.descriptionTextbox = ctk.CTkTextbox(self,font=("Arial",16),width=400,height=200,fg_color="#21244e",
                                                 border_width=1,corner_radius=20)
        self.descriptionTextbox.pack()

        self.dateEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Date: DD/MM/YYYY",width=300,height=30,
                                      corner_radius=30)
        self.dateEntry.pack(pady=20)

        self.reminderSwitch = ctk.CTkCheckBox(self,font=("Arial",14),text="Set a reminder",command=self.onCheck)
        self.reminderSwitch.pack(pady=10)

        self.saveButton = ctk.CTkButton(self,font=("Arial",18),text="Save",command=self.onSaveClick)
        self.saveButton.pack(pady=10)

        # ====== Protocols ======
        self.protocol("WM_DELETE_WINDOW",self.openMenu)
    
    # ====== Methods & Commands ======
    def openMenu(self):
        self.parent.deiconify()
        self.destroy()

    def onCheck(self):
        """ Evaluates when the checkbox is activated if its value is 1 or 0. """
        if self.reminderSwitch.get():
            self.showReminderOption()
        else:
            self.hideReminderOption()

    def showReminderOption(self):
        """ Shows the reminder option. """
        self.saveButton.destroy()

        self.reminderTimeEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Time: HH:MM",width=300,height=30,
                                              corner_radius=30)
        self.reminderTimeEntry.pack(pady=10)

        self.saveButton = ctk.CTkButton(self,font=("Arial",18),text="Save",command=self.onSaveClick)
        self.saveButton.pack(pady=10)

    def hideReminderOption(self):
        """ Hides the reminder option. """
        self.reminderTimeEntry.destroy()

    def onSaveClick(self):
        """ Opens a dialog to confirm and then calls the saveCall function. """
        Dialog(self,title="Save appointment",text=("Are you sure you want to save this appointment?","Yes","No"),
                          func=self.saveCall)
    
    def saveCall(self):
        """ Calls the save appointment function from logic.py file. """
        try:
            logic.saveAppointment(self.edit)
        except Exception:
            Dialog(self,title="Error",text=("Something unexpected happened please try again, or reinstall the application.",
                                            "Ok","Quit"),refusal=exit())

class EditAppointment(ctk.CTkToplevel):
    """ Edit appointment interface. """
    def __init__(self,parent):
        super().__init__(parent)

        # ====== Inicial settings ======
        self.title("Edit appointment")
        self.geometry("700x700")
        self.parent = parent

        # ====== Protocols ======
        self.protocol("WM_DELETE_WINDOW",self.openMenu)
    
    # ====== Methods & Commands ======
    def openMenu(self):
        self.parent.deiconify()
        self.destroy()

class Dialog(ctk.CTkToplevel):
    """ A basic dialog window. """
    def __init__(self,parent,title="Confirmation",text=("","Yes","No"),func=False,refusal=False):
        super().__init__(parent)

        # ====== Inicial settings ======
        self.parent = parent
        self.title(title)
        self.geometry("600x150")
        self.func = func or self.close

        # ====== Widgets ======
        self.textLabel = ctk.CTkLabel(self,font=("Arial Bold",20),text=text[0])
        self.textLabel.pack(pady=10)

        self.acceptButton = ctk.CTkButton(self,font=("Arial",20),text=text[1],
                                          command=self.func)
        self.acceptButton.pack(pady=5,padx=10,side="left")

        self.refuseButton = ctk.CTkButton(self,font=("Arial",20),text=text[2],
                                          command=self.close)
        self.refuseButton.pack(pady=5,padx=10,side="right")

        if refusal: self.refuseButton.configure(command=refusal)

        # ====== Protocols ======
        self.protocol("WM_DELETE_WINDOW",self.close)

    # ====== Methods & Commands
    def close(self):
        self.destroy()

if __name__ == "__main__":
    MainMenu().mainloop()