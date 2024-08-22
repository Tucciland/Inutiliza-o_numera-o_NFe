import pyautogui as ag
from time import sleep
import keyboard

range = 500
numero_inicial = 394666   
numero_final = numero_inicial + range
i=1

def acha_img_e_clica():
    print('Procurando imagem...')
    try:
        img = next(ag.locateAllOnScreen("bt_ok.png", confidence=0.7, region=(700, 350, 200, 200)))
        center_x = img.left + img.width / 2
        center_y = img.top + img.height / 1.3
        ag.click(center_x,center_y,duration=0.5)
        sleep(0.5)
        print('Imagem encontrada!')
        return False
    except:
        sleep(2)
        return True

while numero_final < 4734937:
    print('Rodada ',i)
    ag.click(734, 430, clicks=2, interval=0.2, duration=0.5)
    ag.write(str(numero_inicial)) 

    keyboard.press('tab')
    sleep(0.2)
    ag.write(str(numero_final))  

    ag.click(601, 546, duration=0.5)

    procurar = True
    while procurar:
        procurar = acha_img_e_clica()

    numero_inicial = numero_final + 1
    numero_final = numero_inicial + range
    i=i+1