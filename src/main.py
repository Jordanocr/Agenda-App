import os,art,datetime

def clear():
    """ Basic clear console function. """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Appointment():
    """ Appointment object. """
    def __init__(self,parent,name,description,date):
        self.parent = parent
        self.uid = self.genUid()
        self.name = name
        self.description = description
        self.date = date
    
    def genUid(self):
        """ Generates an uid for the appointment object. """
        return len(self.parent.appointmentList) + 1

class App():
    """ Main application object. """
    def __init__(self):
        self.name = "Agenda"
        self.theme = "roman"
        self.appointmentList = []

    def menu(self):
        """ Main menu interface. """
        while True:
            art.tprint(self.name,self.theme)

            print("Choose an alternative:\n")
            print("1. Create an appointment")
            print("2. List or edit appointments")
            print("3. Information")
            print("4. Quit")

            alt = input("\n> ")
            clear()

            match alt:
                case "1":
                    self.createAppointment()
                case "2":
                    self.editAppointment()
                case "3":
                    self.info()
                case "4":
                    self.quit()
                case _:
                    self.invalidAlternative()
            
    def invalidAlternative(self,msg="Invalid Alternative!"):
        """ Basic dialog interface for errors. """
        clear()
        art.tprint(msg,self.theme)
        input("Press Enter to return ")
        return clear()

    def quit(self):
        """ Basic dialog interface for quitting. """
        while True:
            art.tprint("Quit",self.theme)

            alt = input("Are you sure you want to quit? (y/n) ").lower()
            if alt == "y":
                exit()
            elif alt == "n":
                return clear()
            else:
                self.invalidAlternative()

    def info(self):
        """ Information interface, provides a basic guide on how to use the application. """
        art.tprint("Information",self.theme)

        # ----- Creating new appointments ----- 
        text = """
        \tTo create a new appointment the user should choose the option '1' where the user
        can provide a name which should contain a maximum of 100 characters,a description
        with a maximum of 400 characters, a date in the specified format 'dd/mm/yyyy' 
        and time of the day in the specified format of 'hh/mm'.
        """
        print("\n1. Creating appointments")
        print(text)
        print("\n\n\n")

        # ----- Listing and editing appointments -----
        text = """
        \tTo list and edit already created appointments, the user should choose the option '2'
        where, once the list loads, the user gets to choose to return to menu or type in the
        number of the appointment he wishes to edit. Once he chooses he'll be directed to a
        similar interface to the 'Create appointments' option.
        """
        print("2. Listing and editing appointments")
        print(text)
        print("\n\n\n")

        # ----- Better experience recommendation -----
        text = """
        \tFor a better 'user experience' enter fullscreen mode or maximize the screen
        proportions so the ASCII arts show up correctly.
        """
        print("3. Better experience recommendation")
        print(text)
        print("\n\n\n")

        input("Press Enter to return to menu! ")
        return clear()

    def createAppointment(self,uid=False):
        """ Create appointment method. """
        art.tprint("Create appointment",self.theme)
        
        while True:
            name = input("Name: ")
            if len(name) > 100:
                self.invalidAlternative("Max characters: 100")
                continue
            break

        while True:
            description = input("Description: ")
            if len(description) > 400:
                self.invalidAlternative("Max characters: 400")
                continue
            break

        while True:
            date = input("Date (dd/mm/yyyy): ")
            try:
                datetime.datetime.strptime(date,"%d/%m/%Y").date()
                break
            except ValueError:
                self.invalidAlternative("Invalid Date!")
            
        if uid:
            for appointment in self.appointmentList:
                if appointment.uid == uid:
                    appointment.name = name
                    appointment.description = description
                    appointment.date = date
                    return clear()
        else:
            self.appointmentList.append(Appointment(self,name,description,date))
            return clear()
                                                        
    def editAppointment(self):
        """ Edit appointment method. """
        while True:
            art.tprint("Appointments",self.theme)
            
            if len(self.appointmentList) >= 1:
                for appointment in self.appointmentList:
                    print(f"{appointment.uid}. Appointment: {appointment.name}\n")
                    print(f"Description: {appointment.description}\n")
                    print(f"Date: {appointment.date}\n\n")
            else:
                print("No appointments registered\n")
                input("Press Enter to return to menu!\n")
                return clear()

            print("Press enter to return to menu or choose an appointment to edit!")
            alt = input("\n> ")
            clear()

            if alt == "":
                return clear()

            try:
                for appointment in self.appointmentList:
                    if int(alt) == appointment.uid:
                        self.createAppointment(appointment.uid)
                        return clear()
            except ValueError:
                pass
        
            self.invalidAlternative(f"No appointment!")

if __name__ == "__main__":
    App().menu()

"""
oooooooooo.                 ooooooooo.                            o8o           oooo                           
`888'   `Y8b                `888   `Y88.                          `"'           `888                           
 888     888 oooo    ooo     888   .d88' oooo  oooo  ooo. .oo.   oooo   .oooo.o  888 .oo.    .ooooo.  oooo d8b 
 888oooo888'  `88.  .8'      888ooo88P'  `888  `888  `888P"Y88b  `888  d88(  "8  888P"Y88b  d88' `88b `888""8P 
 888    `88b   `88..8'       888          888   888   888   888   888  `"Y88b.   888   888  888ooo888  888     
 888    .88P    `888'        888          888   888   888   888   888  o.  )88b  888   888  888    .o  888     
o888bood8P'      .8'        o888o         `V88V"V8P' o888o o888o o888o 8""888P' o888o o888o `Y8bod8P' d888b    
             .o..P'                                                                                            
             `Y8P'  
"""
