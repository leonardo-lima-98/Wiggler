import pyautogui
import time
import sys

# Configurações de segurança do PyAutoGUI
pyautogui.FAILSAFE = True  # Permite parar o script movendo o mouse para o canto superior esquerdo
pyautogui.PAUSE = 0.1  # Pequena pausa entre comandos

def obter_centro_tela():
    """Retorna as coordenadas do centro da tela"""
    largura, altura = pyautogui.size()
    return (largura // 2, altura // 2)

def mover_diagonal(x_centro, y_centro):
    """Move o mouse em um padrão diagonal: centro -> diagonal superior direita -> centro"""
    # Move para diagonal superior direita
    pyautogui.moveTo(x_centro + 20, y_centro - 20, duration=0.2)
    # Retorna ao centro
    pyautogui.moveTo(x_centro, y_centro, duration=0.2)

def main():
    print("Monitorando inatividade do mouse...")
    print("Mova o mouse para o canto superior esquerdo para parar o programa.")
    
    x_centro, y_centro = obter_centro_tela()
    ultima_posicao = pyautogui.position()
    tempo_inativo = 0
    
    try:
        while True:
            posicao_atual = pyautogui.position()
            
            # Verifica se o mouse se moveu
            if posicao_atual == ultima_posicao:
                tempo_inativo += 1
            else:
                tempo_inativo = 0
                ultima_posicao = posicao_atual
            
            # Após 5 segundos de inatividade, começa a mover o mouse
            if tempo_inativo >= 300:  # 50 * 0.1 segundos = 5 segundos
                print("Inatividade detectada! Movendo o mouse...")
                pyautogui.moveTo(x_centro, y_centro, duration=0.5)
                mover_diagonal(x_centro, y_centro)
                
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    except pyautogui.FailSafeException:
        print("\nPrograma encerrado pelo failsafe (mouse no canto superior esquerdo).")

if __name__ == "__main__":
    main()