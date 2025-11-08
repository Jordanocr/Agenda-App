import customtkinter as ctk
from CTkTable import *
import webbrowser,logic,random
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

        # ====== Attributes ======
        self.profiles = logic.getUsers()

        # ====== Inicial settings ======
        ctk.set_default_color_theme("src/ui_theme/NightTrain.json")
        ctk.set_appearance_mode("dark")
        self.title(appName)
        self.geometry("500x550")
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
        image = Image.open("src/images/info.png")
        self.profileActivityImage = ctk.CTkImage(image,size=(20,20))
        image = Image.open("src/images/export.png")
        self.exportBackupImage = ctk.CTkImage(image,size=(35,35))

        # ====== Widgets ======
        self.profileFrame = ctk.CTkFrame(self,fg_color="#030515")
        self.profileFrame.pack()

        self.addButton = ctk.CTkButton(self.profileFrame,font=("Arial",15),text="+",width=25,
                                       command=self.openCreateProfile)
        self.addButton.pack(padx=5,side="left")

        self.deleteButton = ctk.CTkButton(self.profileFrame,font=("Arial",15),text="x",width=25,
                                       command=self.openDeleteProfile)
        self.deleteButton.pack(padx=5,side="right")

        self.profileChooser = ctk.CTkOptionMenu(self.profileFrame,width=150,values=self.profiles)
        self.profileChooser.pack(pady=10,side="right")

        Blank(self)

        self.createAppointmentButton = ctk.CTkButton(self,font=("Arial",20),text="Create appointment",
                                                     width=200,height=40,corner_radius=30,image=self.createAppointmentImage,
                                                     border_width=1,command=self.openCreateAppointment)
        self.createAppointmentButton.pack(pady=20)

        self.editAppointmentButton = ctk.CTkButton(self,font=("Arial",20),text="Edit appointments",
                                                   width=200,height=40,corner_radius=30,image=self.editAppointmentImage,
                                                   border_width=1,command=self.openEditAppointment)
        self.editAppointmentButton.pack(pady=20)

        self.profileActivityButton = ctk.CTkButton(self,font=("Arial",20),text="Profile activity",
                                                   width=240,height=40,corner_radius=30,image=self.profileActivityImage,
                                                   border_width=1,command=self.openEditAppointment)
        self.profileActivityButton.pack(pady=20)

        self.exportBackupButton = ctk.CTkButton(self,font=("Arial",20),text="Export backup",
                                                width=240,height=40,corner_radius=30,image=self.exportBackupImage,
                                                border_width=1)
        self.exportBackupButton.pack(pady=20)

        self.githubLabel = ctk.CTkButton(self,font=("Arial",16),text=credits,
                                         width=140,height=28,corner_radius=30,fg_color="transparent",border_width=1,
                                         hover_color="#3b3b3b",command=self.openGithub)
        self.githubLabel.pack(pady=60)

    # ====== Methods & Commands ======
    def openCreateProfile(self):
        """ Opens the create profile interface and hides the main menu. """
        self.withdraw()
        CreateProfile(self)

    def openDeleteProfile(self,boolean=False):
        """ Deletes the selected profile. """
        if not boolean:
            message = "Are you sure you want to delete this profile and agenda?"
            self.dialog = Dialog(self,text=(message,"Yes","No"),func=lambda: self.openDeleteProfile(True))
        else:
            profile = self.profileChooser.get()
            if len(self.profileChooser._values) > 1:
                self.deleteProfileCall(profile)
            else:
                self.dialog.destroy()
                message = "You must have at least one active profile."
                Dialog(self,title="Error",text=(message,"Ok"),geometry="600x100")    

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

class CreateProfile(ctk.CTkToplevel):
    """ Create profile interface. """
    def __init__(self,parent):
        super().__init__(parent)

        # ====== Attributes ======
        title = "Create profile"
        self.parent = parent

        # ====== Inicial settings ======
        self.title(title)
        self.geometry("400x200")
        self.resizable(False,False)

        # ====== Widgets ======
        self.titleLabel = ctk.CTkLabel(self,font=("Arial",40),text=title)
        self.titleLabel.pack(pady=10)

        self.nameEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Name",width=300,height=30,corner_radius=30)
        self.nameEntry.pack(pady=10)

        self.saveButton = ctk.CTkButton(self,font=("Arial",18),text="Save",command=self.onSaveClick)
        self.saveButton.pack(pady=10)

        # ====== Protocols ======
        self.protocol("WM_DELETE_WINDOW",self.openMenu)

    # ====== Methods & Commands ======
    def openMenu(self):
        """ Opens menu then destroys itself. """
        self.parent.deiconify()
        self.destroy()
    
    def onSaveClick(self):
        """ Calls the saveCall function. """
        pass

class CreateAppointment(ctk.CTkToplevel):
    """ Create appointment interface. """
    def __init__(self,parent,edit=False):
        super().__init__(parent)

        # ====== Attributes ======
        title = "Create appointment"
        self.parent = parent
        self.edit = edit

        # ====== Inicial settings ======
        self.title(title)
        self.geometry("700x650")

        # ====== Widgets ======
        self.titleLabel = ctk.CTkLabel(self,font=("Arial",40),text=title)
        self.titleLabel.pack(pady=10)

        Blank(self,py=10)

        self.nameEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Name",width=400,height=30,corner_radius=30)
        self.nameEntry.pack(pady=10)

        self.descriptionLabel = ctk.CTkLabel(self,font=("Arial",16),text="Description:")
        self.descriptionLabel.pack(pady=5,padx=170,anchor="nw")

        self.descriptionTextbox = ctk.CTkTextbox(self,font=("Arial",14),width=400,height=200,fg_color="#21244e",
                                                 border_width=1,corner_radius=20)
        self.descriptionTextbox.pack()

        self.dateEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Date DD/MM/YYYY",width=400,height=30,
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
        """ Opens menu then destroys itself. """
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
        self.saveButton.pack_forget()

        self.reminderTimeEntry = ctk.CTkEntry(self,font=("Arial",18),placeholder_text="Time HH:MM",width=400,height=30,
                                              corner_radius=30)
        self.reminderTimeEntry.pack(pady=10)

        self.saveButton = ctk.CTkButton(self,font=("Arial",18),text="Save",command=self.onSaveClick)
        self.saveButton.pack(pady=10)

    def hideReminderOption(self):
        """ Hides the reminder option. """
        self.reminderTimeEntry.destroy()

    def onSaveClick(self):
        """ Opens a dialog to confirm and then calls the saveCall function. """
        text = ("Are you sure you want to save this appointment?","Yes","No")
        self.dialog = Dialog(self,title="Save appointment",text=text,
                          func=self.saveCall)
    
    def saveCall(self):
        """ Calls the save appointment function from logic.py file and destroys the dialog save window. """
        self.dialog.destroy()
        try:
            logic.saveAppointment(self.edit)
        except Exception:
            self.errorCallback()
        
    def errorCallback(self):
        """ Called by the logic.py file in case an error happens. """
        text = "Something unexpected happened, please try again or reinstall the application."
        Dialog(self,title="Error",text=(text,"Ok","Quit"),refusal=exit,geometry="850x150")
        
class EditAppointment(ctk.CTkToplevel):
    """ Edit appointment interface. """
    def __init__(self,parent):
        super().__init__(parent)

        # ====== Attributes ======
        title = "Edit appointment"
        self.parent = parent

        # ====== Inicial settings ======
        self.title(title)
        self.geometry("700x650")
        self.withdraw() # So that it can load everything first

        # ====== Widgets ======
        self.titleLabel = ctk.CTkLabel(self,font=("Arial",40),text=title)
        self.titleLabel.pack(pady=10)

        listValues = [["Name","Date","Time"],
                      ["A","07/11/2025","21:51"],
                      ["B","08/11/2025","22:30"],
                      ["C","09/11/2025","23:00"]]
        self.nameValues = []

        for value in listValues:
            if value[0] != "Name":
                self.nameValues.append(value[0])

        self.tableFrame = ctk.CTkScrollableFrame(self,width=400,height=400,fg_color="#030515")
        self.tableFrame.pack(pady=10)

        self.appointmentTable = CTkTable(self.tableFrame,values=listValues,width=140,height=40,header_color="#21244e")
        self.appointmentTable.pack(pady=10)

        self.editComboBox = ctk.CTkComboBox(self,values=self.nameValues)
        self.editComboBox.pack(pady=20)

        self.editButton = ctk.CTkButton(self,font=("Arial",18),text="Edit or View")
        self.editButton.pack(pady=20)

        self.update_idletasks() # Guarantees that the widgets are packed geometrically before showing the window.
        self.deiconify()

        # ====== Protocols ======
        self.protocol("WM_DELETE_WINDOW",self.openMenu)
    
    # ====== Methods & Commands ======
    def openMenu(self):
        """ Opens menu then destroys itself. """
        self.parent.deiconify()
        self.destroy()
    
    def editAppointment(self,appointmentName):
        if appointmentName in self.nameValues:
            edit = logic.getAppointment(appointmentName)
            CreateAppointment()
        else:
            pass

class Dialog(ctk.CTkToplevel):
    """ A basic dialog window. """
    def __init__(self,parent,title="Confirmation",text=("","Yes","No"),func=False,refusal=False,geometry="600x150"):
        super().__init__(parent)

        # ====== Attributes ======
        self.parent = parent
        self.func = func or self.close

        # ====== Inicial settings ======
        self.title(title)
        self.geometry(geometry)
        self.resizable(False,False)
        self.after(10,self.grab_set)

        # ====== Widgets ======
        self.textLabel = ctk.CTkLabel(self,font=("Arial Bold",20),text=text[0])
        self.textLabel.pack(pady=10)

        self.acceptButton = ctk.CTkButton(self,font=("Arial",20),text=text[1],
                                          command=self.func)
        self.acceptButton.pack(pady=5,padx=10)

        if len(text) >= 3:
            """ Creates the refuse button if not configured beforehand and
            repacks the accept button as non-unique confirmation button. """

            self.acceptButton.pack_configure(pady=5,padx=10,side="left")

            self.refuseButton = ctk.CTkButton(self,font=("Arial",20),text=text[2],
                                            command=self.close)
            self.refuseButton.pack(pady=5,padx=10,side="right")

            if refusal: self.refuseButton.configure(command=refusal)

        # ====== Protocols ======
        self.protocol("WM_DELETE_WINDOW",self.close)

    # ====== Methods & Commands
    def close(self):
        """ Destroys itself. """
        self.destroy()

if __name__ == "__main__":
    MainMenu().mainloop()