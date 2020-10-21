from infi.systray import SysTrayIcon
from tkinter import *


def open_chat(systray):
    chatBot = Tk()
    def send():
        send = "You => " + e.get()
        txt.insert(END,"\n" + send)
        e.delete(0,END)
    chatBot.title("Prot3ctingInbox3s Chat Service")
    chatBot.iconbitmap(r"logof.ico")
    chatBot.resizable(False, False)
    txt = Text(chatBot)
    txt.grid(row=0,column=0,columnspan=2)
    e = Entry(chatBot,width=100)
    send = Button(chatBot,text="Send",command=send).grid(row=1,column=1)
    e.grid(row=1,column=0)
    chatBot.mainloop()
   
def show_settings(systray):
    settingsWind = Tk()
    settingsWind.title("Prot3ctingInbox3s Settings")
    settingsWind.iconbitmap(r"logof.ico")
def show_logs(systray):
    logsWind = Tk()
    logsWind.title("Prot3ctingInbox3s Logs")
    logsWind.iconbitmap(r"logof.ico")


       
menu_options = (("Open Chat", None, open_chat),("Settings", None, show_settings),("Show Logs", None, show_logs))
systray = SysTrayIcon("logof.ico", "Prot3ctingInbox3s", menu_options, default_menu_index=0)
systray.start()

