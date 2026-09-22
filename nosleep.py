import rumps
import subprocess

#creates a menu bar app 
class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Preferences") #to be worked on later
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")


    def no_multi_caffeinate_indef(self, sender):
        pkill = subprocess.Popen(["pkill", "caffeinate"])
        pkill.wait()
        subprocess.Popen(["caffeinate", "-d"])

    def no_multi_caffeinate_1h(self, sender):
        pkill = subprocess.Popen(["pkill", "caffeinate"])
        pkill.wait()
        subprocess.Popen(["caffeinate", "-t", "3600"])

#indefinite
    @rumps.clicked("Turn On NoSleep Indefinitely") #turns on NoSleep indefinitely (until the user toggles it off)
    def turn_on(self, sender):
            self.caffeinate_process = subprocess.Popen(["caffeinate", "-d"])
            sender.state = True
            rumps.alert("NoSleep Toggled on") 
            if rumps.clicked("Turn On NoSleep Indefinitely") and sender.state == True:
                self.no_multi_caffeinate_indef(sender)


#1 hour
    @rumps.clicked("Turn On NoSleep for 1 Hour") #turns on NoSleep for 1 hour (until the user toggles it off)
    def turn_on_1_hour(self, sender):
            self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "3600"])
            sender.state = True
            rumps.alert("NoSleep Toggled on") 
            if rumps.clicked("Turn On NoSleep for 1 Hour") and sender.state == True:  
                self.no_multi_caffeinate_1h(sender)


#30 minutes


    #this part works fine as is
    @rumps.clicked("Turn Off NoSleep") #turns off NoSleep (until the user toggles it on)
    def turn_off(self, sender):
            self.caffeinate_process.terminate()
            self.caffeinate_process.wait()
            self.caffeinate_process = None
            sender.state = False
            rumps.alert("NoSleep Toggled off")

if __name__ == "__main__":
    AwesomeStatusBarApp("NoSleep").run()