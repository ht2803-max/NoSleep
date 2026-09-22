import rumps
import subprocess

#creates a menu bar app 
class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Preferences") #to be worked on later
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Turn On NoSleep Indefinitely") #turns on NoSleep indefinitely (until the user toggles it off)
    def turn_on(self, sender):
            subprocess.Popen(["caffeinate", "-d"])
            sender.state = True
            rumps.alert("NoSleep Toggled on") 

            
    @rumps.clicked("Turn Off NoSleep") #turns off NoSleep (until the user toggles it on)
    def turn_off(self, sender):
            subprocess.run(["pkill", "caffeinate"])
            sender.state = False
            rumps.alert("NoSleep Toggled off")

if __name__ == "__main__":
    AwesomeStatusBarApp("NoSleep").run()