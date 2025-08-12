import pyautogui 
import time
import subprocess

steam_path = r"C:\Program Files (x86)\Steam\Steam.exe" #Can change depending on computer settings

try: 
    subprocess.Popen(steam_path)
    time.sleep(10)
except FileNotFoundError:
    print("Steam not found")
    exit()

print("Procurando o botão na tela...")
botao_comunidade = None
while botao_comunidade is None:
    try:
        botao_comunidade = pyautogui.locateOnScreen('screenshots/comunity_ss.JPG', confidence=0.9)
        if botao_comunidade:
            print("Botão encontrado!")
        else:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)
    except pyautogui.ImageNotFoundException:
        print("Botão não encontrado. Tentando novamente em 3 segundos...")
        time.sleep(3)

if botao_comunidade:
    
    centro_do_botao = pyautogui.center(botao_comunidade)
    
    print(f"Clicando nas coordenadas: {centro_do_botao.x}, {centro_do_botao.y}")
    # Simula um clique do mouse
    pyautogui.click(centro_do_botao)
    
    print("Botao clicado kekw!")
else:
    print("Não foi possível encontrar o botão após várias tentativas.")

print("Procurando o filho da puta")
pesquisa_amigos = None
while pesquisa_amigos == None:
    try:
        pesquisa_amigos = pyautogui.locateOnScreen('screenshots/find_friends_ss.JPG', confidence=0.9)
        if pesquisa_amigos:
            print("Botão encontrado!")
        else:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)
    except pyautogui.ImageNotFoundException:
        print("Botão não encontrado. Tentando novamente em 3 segundos...")
        time.sleep(3)

if pesquisa_amigos:
    
    centro_da_pesquisa = pyautogui.center(pesquisa_amigos)
    nick_do_corno = "bolsonaro2018x"
    print(f"Clicando nas coordenadas: {centro_da_pesquisa.x}, {centro_da_pesquisa.y}")
    # Simula um clique do mouse
    pyautogui.click(centro_da_pesquisa)
    print("Botao clicado kekw!")
    pyautogui.write(nick_do_corno)
    print("colou???")
    pyautogui.hotkey('enter')
else:
    print("Não foi possível encontrar o botão após várias tentativas.")

avatar_corno = None
while avatar_corno == None:
    try:
        avatar_corno = pyautogui.locateOnScreen('screenshots/avatar_corno_ss.JPG', confidence=0.9)
        centro_do_corno = pyautogui.center(avatar_corno)
        pyautogui.click(centro_do_corno)
        print("Botao clicado kekw!")
    except pyautogui.ImageNotFoundException:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)

mais_botao = None
while mais_botao == None:
    try:
        mais_botao = pyautogui.locateOnScreen('screenshots/mais_ss.JPG', confidence=0.9)
        centro_do_mais = pyautogui.center(mais_botao)
        pyautogui.click(centro_do_mais)
        print("Botao clicado kekw!")
        time.sleep(2)
        for i in range(5):
            pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
    except pyautogui.ImageNotFoundException:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)

# denuncia_botao = None
# while denuncia_botao == None:
#     try:
#         denuncia_botao = pyautogui.locateOnScreen('screenshots/denuncia_player.JPG', confidence=0.9)
#         centro_do_denuncia = pyautogui.center(denuncia_botao)
#         pyautogui.click(centro_do_denuncia)
#         print("Botao clicado kekw!")
#         time.sleep(3)
#     except pyautogui.ImageNotFoundException:
#             print("Botão não encontrado. Tentando novamente em 3 segundos...")
#             time.sleep(3)

batota_botao = None
while batota_botao == None:
    try:
        batota_botao = pyautogui.locateOnScreen('screenshots/batota_ss.JPG', confidence=0.9)
        centro_do_batota = pyautogui.center(batota_botao)
        pyautogui.click(centro_do_batota)
        print("Botao clicado kekw!")
        time.sleep(3)
    except pyautogui.ImageNotFoundException:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)

denuncia_final = None
while denuncia_final == None:
    try:
        denuncia_final = pyautogui.locateOnScreen('screenshots/denunciar_final_ss.JPG', confidence=0.9)
        centro_do_denuncia_final = pyautogui.center(denuncia_final)
        pyautogui.click(centro_do_denuncia_final)
        print("Botao clicado kekw!")
        text_denuncia = "Fez uso de wallhack (conseguia visualizar através das paredes) e uso de aimbot (mira ajustada automaticamente para matar os adversários);"
        time.sleep(3)
        pyautogui.write(text_denuncia)
        time.sleep(3)
        pyautogui.hotkey('enter')
    except pyautogui.ImageNotFoundException:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)

cs_botao = None
while cs_botao == None:
    try:
        cs_botao = pyautogui.locateOnScreen('screenshots/game_denuncia.JPG', confidence=0.9)
        centro_do_cs = pyautogui.center(cs_botao)
        pyautogui.click(centro_do_cs)
        print("Botao clicado kekw!")
        time.sleep(1)
        enviar_denuncia = pyautogui.locateOnScreen('screenshots/enviar_denuncia_ss.JPG', confidence=0.9)
        centro_do_enviar = pyautogui.center(enviar_denuncia)
        pyautogui.click(centro_do_enviar)
        print("Botao clicado kekw!")
    except pyautogui.ImageNotFoundException:
            print("Botão não encontrado. Tentando novamente em 3 segundos...")
            time.sleep(3)