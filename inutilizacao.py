import pyautogui as ag
from time import sleep
import keyboard

numero_inicial = 20534   
numero_final = numero_inicial + 500

while numero_final < 4734937:
    ag.click(734, 430, clicks=2, interval=0.2, duration=0.5)
    ag.write(str(numero_inicial)) 

    keyboard.press('tab')
    sleep(0.2)
    ag.write(str(numero_final))  

    ag.click(601, 546, duration=0.5)
    
    sleep(40)
    
    ag.click(812, 457, duration=0.5)

    numero_inicial = numero_final + 1
    numero_final = numero_inicial + 500