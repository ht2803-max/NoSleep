import rumps
import subprocess
import os
from shutil import which
from AppKit import NSApplication
from settings_preview import SettingsWindowController

#creates a menu bar app
class AwesomeStatusBarApp(rumps.App):

    def no_multi_caffeinate_indef(self, sender): #prevents multiple instances of caffeinate from running at the same time for indefinite (which would cause issues)
        pkill = subprocess.Popen(["pkill", "caffeinate"])
        pkill.wait()
        subprocess.Popen(["caffeinate", "-d"])

    def no_multi_caffeinate_xh(self, hours): #prevents multiple instances of caffeinate from running at the same time for x hours (which would cause issues)
        pkill = subprocess.Popen(["pkill", "caffeinate"])
        pkill.wait()
        subprocess.Popen(["caffeinate", "-t", str(hours * 3600)])

    def no_multi_caffeinate_xm(self, minutes): #prevents multiple instances of caffeinate from running at the same time for x minutes (which would cause issues)
        pkill = subprocess.Popen(["pkill", "caffeinate"])
        pkill.wait()
        subprocess.Popen(["caffeinate", "-t", str(minutes * 60)])

#indefinite
    @rumps.clicked("NoSleep Indefinitely") #turns on NoSleep indefinitely (until the user toggles it off)
    def turn_on(self, sender):
            self.caffeinate_process = subprocess.Popen(["caffeinate", "-d"])
            sender.state = True
            rumps.alert("NoSleep Toggled on") 
            if rumps.clicked("Turn On NoSleep Indefinitely") and sender.state == True:
                self.no_multi_caffeinate_indef(sender)


#hours
       
    @rumps.clicked("(Hours) NoSleep for", "1 hour")
    def one_hour(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "3600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on") 
        if rumps.clicked("No Sleep", "1 hour") and sender.state == True:
            self.no_multi_caffeinate_xh(1)

    @rumps.clicked("(Hours) NoSleep for", "2 hours")
    def two_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "7200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "2 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(2)

    @rumps.clicked("(Hours) NoSleep for", "3 hours")
    def three_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "10800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "3 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(3)

    @rumps.clicked("(Hours) NoSleep for", "4 hours")
    def four_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "14400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "4 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(4)

    @rumps.clicked("(Hours) NoSleep for", "5 hours")
    def five_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "18000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "5 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(5)

    @rumps.clicked("(Hours) NoSleep for", "6 hours")
    def six_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "21600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "6 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(6)

    @rumps.clicked("(Hours) NoSleep for", "7 hours")
    def seven_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "25200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "7 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(7)

    @rumps.clicked("(Hours) NoSleep for", "8 hours")
    def eight_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "28800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "8 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(8)

    @rumps.clicked("(Hours) NoSleep for", "9 hours")
    def nine_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "32400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "9 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(9)

    @rumps.clicked("(Hours) NoSleep for", "10 hours")
    def ten_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "36000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "10 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(10)

    @rumps.clicked("(Hours) NoSleep for", "11 hours")
    def eleven_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "39600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "11 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(11)

    @rumps.clicked("(Hours) NoSleep for", "12 hours")
    def twelve_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "43200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "12 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(12)

    @rumps.clicked("(Hours) NoSleep for", "13 hours")
    def thirteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "46800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "13 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(13)

    @rumps.clicked("(Hours) NoSleep for", "14 hours")
    def fourteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "50400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "14 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(14)

    @rumps.clicked("(Hours) NoSleep for", "15 hours")
    def fifteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "54000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "15 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(15)

    @rumps.clicked("(Hours) NoSleep for", "16 hours")
    def sixteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "57600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "16 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(16)

    @rumps.clicked("(Hours) NoSleep for", "17 hours")
    def seventeen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "61200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "17 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(17)

    @rumps.clicked("(Hours) NoSleep for", "18 hours")
    def eighteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "64800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "18 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(18)

    @rumps.clicked("(Hours) NoSleep for", "19 hours")
    def nineteen_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "68400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "19 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(19)
    
    @rumps.clicked("(Hours) NoSleep for", "20 hours")
    def twenty_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "72000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "20 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(20)

    @rumps.clicked("(Hours) NoSleep for", "21 hours")
    def twentyone_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "75600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "21 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(21)

    @rumps.clicked("(Hours) NoSleep for", "22 hours")
    def twentytwo_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "79200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "22 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(22)

    @rumps.clicked("(Hours) NoSleep for", "23 hours")
    def twentythree_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "82800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "23 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(23)

    @rumps.clicked("(Hours) NoSleep for", "24 hours")
    def twentyfour_hours(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "86400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "24 hours") and sender.state == True:
            self.no_multi_caffeinate_xh(24)


#X minutes

    @rumps.clicked("(Minutes) NoSleep for", "1 Minute")
    def one_minute(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "60"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "1 Minute") and sender.state == True:
            self.no_multi_caffeinate_xm(1)
    
    @rumps.clicked("(Minutes) NoSleep for", "5 minutes")
    def five_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "300"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "5 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(5)

    @rumps.clicked("(Minutes) NoSleep for", "10 minutes")
    def ten_min(self, sender): 
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "10 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(10)

    @rumps.clicked("(Minutes) NoSleep for", "15 minutes")
    def fifteen_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "900"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "15 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(15)

    @rumps.clicked("(Minutes) NoSleep for", "20 minutes")
    def twenty_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "1200"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "20 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(20)

    @rumps.clicked("(Minutes) NoSleep for", "25 minutes")
    def twentyfive_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "1500"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "25 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(25)

    @rumps.clicked("(Minutes) NoSleep for", "30 minutes")
    def thirty_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "1800"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "30 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(30)

    @rumps.clicked("(Minutes) NoSleep for", "35 minutes")
    def thirtyfive_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "2100"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "35 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(35)

    @rumps.clicked("(Minutes) NoSleep for", "40 minutes")
    def forty_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "2400"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "40 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(40)

    @rumps.clicked("(Minutes) NoSleep for", "45 minutes")
    def fortyfive_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "2700"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "45 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(45)

    @rumps.clicked("(Minutes) NoSleep for", "50 minutes")
    def fifty_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "3000"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "50 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(50)

    @rumps.clicked("(Minutes) NoSleep for", "55 minutes")
    def fiftyfive_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "3300"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "55 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(55)

    @rumps.clicked("(Minutes) NoSleep for", "60 minutes")
    def sixty_min(self, sender):
        self.caffeinate_process = subprocess.Popen(["caffeinate", "-t", "3600"])
        sender.state = True
        rumps.alert("NoSleep Toggled on")
        if rumps.clicked("No Sleep", "60 minutes") and sender.state == True:
            self.no_multi_caffeinate_xm(60)

    @rumps.clicked("Settings")
    def show_settings(self, _):
        if not hasattr(self, "settings_controller"):
            self.settings_controller = SettingsWindowController.alloc().init()
        self.settings_controller.window.makeKeyAndOrderFront_(None)
        NSApplication.sharedApplication().activateIgnoringOtherApps_(True)


    @rumps.clicked("Turn Off NoSleep") #turns off NoSleep (until the user toggles it on)
    def turn_off(self, sender):
            pkill = subprocess.Popen(["pkill", "caffeinate"])
            pkill.wait()
            sender.state = False
            rumps.alert("NoSleep Toggled off")


if __name__ == "__main__":
    AwesomeStatusBarApp("NoSleep").run()
