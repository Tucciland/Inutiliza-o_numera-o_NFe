import pyautogui as ag
from time import sleep
import keyboard

#Declaração das variaveis de numero inicial e final e o contador para contar as execuções.
range = 500
numero_inicial = 394666   
numero_final = numero_inicial + range
i=1

#Função responsavel por procurar a imagem de sucesso na inutilização do software utilizado.
def acha_img_e_clica():
    print('Procurando imagem...')
    try:
        img = next(ag.locateAllOnScreen("bt_ok.png", confidence=0.7, region=(700, 350, 200, 200)))
        
        #Calculo para onde o botão fica de acordo com a imagem encontrada.
        center_x = img.left + img.width / 2
        center_y = img.top + img.height / 1.3
        ag.click(center_x,center_y,duration=0.5)
        sleep(0.5)
        print('Imagem encontrada!')
        return False
    except:
        sleep(2)
        return True

#Loop que fica realizando as interações na tela necessarias para fazer as inutilizações no software. 
#até que o numero de inutilizações que o cliente precisa seja atingido.
while numero_final < 4734937:
    
    print('Rodada ',i)

    #Clica no campo do numero inicial e escreve o valor.
    ag.click(734, 430, clicks=2, interval=0.2, duration=0.5)
    ag.write(str(numero_inicial)) 

    #Pressiona o tab para pular pro campo de numero final e escreve o valor.
    keyboard.press('tab')
    sleep(0.2)
    ag.write(str(numero_final))  

    #Clique para iniciar o processo de inutilização.
    ag.click(601, 546, duration=0.5)

    #Loop que fica constantemente procurando se não encontrar retorna 'True' e executa novamente se encontrar retorna 'False' e interrompe o loop.
    procurar = True
    while procurar:
        procurar = acha_img_e_clica()

    #Ajeita o numero inicial e final para a proxima inutilização.
    numero_inicial = numero_final + 1
    numero_final = numero_inicial + range
    i=i+1