#!/usr/bin/python3
# By Hooksander

from datetime import datetime
import os
import time
import platform

def main() :
    now = str(datetime.now())
    hour = int(now[11:13])
    minute = int(now[14:16])
    second = now[17:19]
    print("Il est {} heure {} et {} secondes\n\n".format(hour, minute, second))
    currentOs = platform.system()
    
    print("A quelle heure souhaitez vous que l'ordinateur s'arrête ?\n")
    while True :
        shutdownTime = input("Entrer la sous le format HH:MM\n=> ")
        shutdownHour = int(shutdownTime[0:2])
        shutdownMinute = int(shutdownTime[3:6])
        if shutdownHour < 0 or shutdownHour > 24 :
            print("L'heure est incorrect\n")
        if shutdownMinute < 0 or shutdownMinute > 60 :
            print("Les minutes sont incorrect\n")
        else :
            break
    while True :
        currentHour = int(str(datetime.now())[11:13])
        currentMinute = int(str(datetime.now())[14:16])
        if shutdownHour == currentHour :
            if shutdownMinute == currentMinute :
                if currentOs == 'Linux' :
                    os.system("shutdown now")
                    break
                if currentOs == 'Windows' :
                    os.system("shutdown /s /t 0")
                    break
                else : 
                    print("System d'exploitation non supporté.")
                    break
        time.sleep(10)
    exit()
    
if __name__ == '__main__' :
    main()