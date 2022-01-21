from lundi import monday
from mardi import tuesday
from mercredi import wednesday
from jeudi import thursday
from vendredi import friday
import time
from datetime import datetime
from pynput.keyboard import Controller
import webbrowser

keyboard = Controller()

day_of_the_week = datetime.today().weekday()

if day_of_the_week == 0:
    while day_of_the_week == 1:
        for i in monday:
            while True:
                if datetime.now().hour > int(i[1].split(':')[0]):
                    continue
                if datetime.now().hour == int(i[1].split(':')[0]):
                    if datetime.now().minute > int(i[1].split(':')[1]):
                        continue
                    if datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        break
                    time.sleep(5)
        break

elif day_of_the_week == 1:
    while day_of_the_week == 1:
        for i in tuesday:
            while True:
                if datetime.now().hour > int(i[1].split(':')[0]):
                    continue
                if datetime.now().hour == int(i[1].split(':')[0]):
                    if datetime.now().minute > int(i[1].split(':')[1]):
                        continue
                    if datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        break
                    time.sleep(5)
        break

elif day_of_the_week == 2:
    while day_of_the_week == 2:
        for i in wednesday:
            while True:
                if datetime.now().hour > int(i[1].split(':')[0]):
                    continue
                if datetime.now().hour == int(i[1].split(':')[0]):
                    if datetime.now().minute > int(i[1].split(':')[1]):
                        continue
                    if datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        break
                    time.sleep(5)
        break

elif day_of_the_week == 3:
    while day_of_the_week == 3:
        for i in thursday:
            while True:
                if datetime.now().hour > int(i[1].split(':')[0]):
                    continue
                if datetime.now().hour == int(i[1].split(':')[0]):
                    if datetime.now().minute > int(i[1].split(':')[1]):
                        continue
                    if datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        break
                    time.sleep(5)
        break

elif day_of_the_week == 4:
    while day_of_the_week == 4:
        for i in friday:
            while True:
                if datetime.now().hour > int(i[1].split(':')[0]):
                    continue
                if datetime.now().hour == int(i[1].split(':')[0]):
                    if datetime.now().minute > int(i[1].split(':')[1]):
                        continue
                    if datetime.now().minute == int(i[1].split(':')[1]):
                        webbrowser.open(i[0])
                        break
                    time.sleep(5)
        break