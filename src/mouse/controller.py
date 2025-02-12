# src/mouse/controller.py
import pyautogui
import time

class MouseController:
    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1
        
    def get_screen_center(self):
        width, height = pyautogui.size()
        return (width // 2, height // 2)
        
    def move_diagonal(self, x_center, y_center, app):
        """Move o mouse em um padrão diagonal"""
        if app.is_running():
            pyautogui.moveTo(x_center + 20, y_center - 20, duration=0.5)
            if app.is_running():
                pyautogui.moveTo(x_center, y_center, duration=0.5)
                
    def monitor_mouse(self, app, get_inactive_time, update_status, stop_callback):
        x_center, y_center = self.get_screen_center()
        last_position = pyautogui.position()
        inactive_time = 0
        
        while app.is_running():  # Usando o método is_running do app
            try:
                current_position = pyautogui.position()
                
                if current_position == last_position:
                    inactive_time += 1
                else:
                    inactive_time = 0
                    last_position = current_position
                
                inactive_seconds = get_inactive_time()
                if inactive_time >= inactive_seconds * 10:
                    update_status("Movendo mouse")
                    pyautogui.moveTo(x_center, y_center, duration=0.5)
                    self.move_diagonal(x_center, y_center, app)
                else:
                    update_status("Monitorando")
                    
                time.sleep(0.1)
                
            except pyautogui.FailSafeException:
                stop_callback()
                break
            except Exception as e:
                print(f"Erro: {e}")
                stop_callback()
                break