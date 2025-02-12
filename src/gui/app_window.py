# src/gui/app_window.py
from tkinter import ttk
from .widgets import StatusLabel, ControlFrame, SettingsFrame
from ..mouse.controller import MouseController
import threading

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Mouse Mover")
        self.root.geometry("300x200")
        
        self.running = False
        self.monitoring_thread = None
        
        self.mouse_controller = MouseController()
        self.create_widgets()
        
    def create_widgets(self):
        # Status
        self.status_label = StatusLabel(self.root)
        self.status_label.pack(pady=10)
        
        # Controles
        self.control_frame = ControlFrame(self.root, self.toggle_monitoring)
        self.control_frame.pack(pady=10)
        
        # Configurações
        self.settings_frame = SettingsFrame(self.root)
        self.settings_frame.pack(padx=10, pady=5, fill="x")
        
        # Informações
        info_text = ("Para parar o programa:\n"
                    "1. Clique no botão 'Parar'\n"
                    "2. Ou mova o mouse para o canto superior esquerdo")
        info_label = ttk.Label(self.root, text=info_text, justify="left")
        info_label.pack(pady=10)

    def toggle_monitoring(self):
        if not self.running:
            self.running = True
            self.control_frame.update_button_text("Parar")
            self.monitoring_thread = threading.Thread(
                target=self.mouse_controller.monitor_mouse,
                args=(
                    self,  # Passando self ao invés de self.running
                    self.settings_frame.get_inactive_time,
                    self.status_label.update_status,
                    self.stop_monitoring
                )
            )
            self.monitoring_thread.start()
        else:
            self.stop_monitoring()

    def stop_monitoring(self):
        self.running = False
        self.control_frame.update_button_text("Iniciar")
        self.status_label.update_status("Parado")
        if self.monitoring_thread:
            self.monitoring_thread.join()

    def on_closing(self):
        self.stop_monitoring()
        self.root.destroy()

    def is_running(self):  # Novo método
        return self.running