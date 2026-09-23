from unicodedata import name
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

    def no_multi_caffeinate_xh(self, sender):
        pkill = subprocess.Popen(["pkill", "caffeinate"])
        pkill.wait()
        subprocess.Popen(["caffeinate", "-t", "3600"])

#indefinite
    @rumps.clicked("NoSleep Indefinitely") #turns on NoSleep indefinitely (until the user toggles it off)
    def turn_on(self, sender):
            self.caffeinate_process = subprocess.Popen(["caffeinate", "-d"])
            sender.state = True
            rumps.alert("NoSleep Toggled on") 
            if rumps.clicked("Turn On NoSleep Indefinitely") and sender.state == True:
                self.no_multi_caffeinate_indef(sender)


#hours
    @rumps.clicked("NoSleep X Hours") #turns on NoSleep for X hour (until the user toggles it off)
    def __init__(self, name):
            super().__init__(
                name,
                menu=[
                    ("NoSleep for", ["1 hour", "2 hours", "3 hours", "4 hours", "5 hours", "6 hours", "7 hours", "8 hours", "9 hours", "10 hours", "11 hours", "12 hours", "13 hours", "14 hours", "15 hours", "16 hours", "17 hours", "18 hours", "19 hours", "20 hours", "21 hours", "22 hours", "23 hours", "24 hours"])
                ],
            )

        
    @rumps.clicked("NoSleep for", "1 hour")
    def one_hour(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "3600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on") 
        if rumps.clicked("No Sleep", "1 hour") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "2 hours")
    def two_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "7200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "2 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "3 hours")
    def three_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "10800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "3 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "4 hours")
    def four_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "14400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "4 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "5 hours")
    def five_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "18000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "5 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "6 hours")
    def six_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "21600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "6 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "7 hours")
    def seven_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "25200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "7 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "8 hours")
    def eight_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "28800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "8 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "9 hours")
    def nine_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "32400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "9 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "10 hours")
    def ten_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "36000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "10 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "11 hours")
    def eleven_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "39600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "11 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "12 hours")
    def twelve_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "43200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "12 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "13 hours")
    def thirteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "46800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "13 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "14 hours")
    def fourteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "50400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "14 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "15 hours")
    def fifteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "54000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "15 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "16 hours")
    def sixteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "57600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "16 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "17 hours")
    def seventeen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "61200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "17 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "18 hours")
    def eighteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "64800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "18 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)

    @rumps.clicked("NoSleep for", "19 hours")
    def nineteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "68400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "19 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    

    @rumps.clicked("NoSleep for", "20 hours")
    def twenty_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "72000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "20 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "21 hours")
    def twentyone_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "75600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "21 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "22 hours")
    def twentytwo_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "79200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "22 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "23 hours")
    def twentythree_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "82800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "23 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)
    
    @rumps.clicked("NoSleep for", "24 hours")
    def twentyfour_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "86400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "24 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(sender)


#X minutes

    #this part works fine as is
    @rumps.clicked("Turn Off NoSleep") #turns off NoSleep (until the user toggles it on)
    def turn_off(self, sender):
            pkill = subprocess.Popen(["pkill", "caffeinate"])
            pkill.wait()
            sender.state = False
            rumps.alert("NoSleep Toggled off")

if __name__ == "__main__":
    AwesomeStatusBarApp("NoSleep").run()