import PySimpleGUI as sg
import win32api
import sys

from datetime import datetime

# todos:
#   handle valueError (minute must be in 0..59)

def set_time(cooldown):
    now = datetime.now()
    time_tuple = (now.year, now.month, now.day, now.hour - 2, now.minute + cooldown, now.second, 0)
    dayOfWeek = datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    win32api.SetSystemTime(*t)

layout = [
    [sg.Text("choose cooldown time")],
    [sg.Button("5")],
    [sg.Button("10")],
    [sg.Button("30")],
    [sg.Button("RESET")]
]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()

    if event == "5":
        set_time(5)
    if event == "10":
        set_time(10)
    if event == "30":
        set_time(30)
    if event == "RESET":
        print("todo")
    if event == sg.WIN_CLOSED:
        break

window.close()
