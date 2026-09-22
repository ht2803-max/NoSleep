import rumps
import subprocess

#creates a menu bar app 
class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Preferences") #to be worked on later
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")


#this part has an issue where if u press the button mutiple times, it will start multiple caffeinate processes. 
    @rumps.clicked("Turn On NoSleep Indefinitely") #turns on NoSleep indefinitely (until the user toggles it off)
    def turn_on(self, sender):
            self.caffeinate_process = subprocess.Popen(["caffeinate", "-d"])
            sender.state = True
            rumps.alert("NoSleep Toggled on") 
            if rumps.clicked("Turn On NoSleep Indefinitely") and sender.state == True:  #should fix later bc this closes all available caffeinate processes, but for now it works
                pkill = subprocess.Popen(["pkill", "caffeinate"])
                pkill.wait()
                subprocess.Popen(["caffeinate", "-d"])

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