# src/gui/widgets.py
import tkinter as tk
from tkinter import ttk

class StatusLabel:
    def __init__(self, parent):
        self.label = ttk.Label(parent, text="Status: Parado", font=('Arial', 10))
        
    def pack(self, **kwargs):
        self.label.pack(**kwargs)
        
    def update_status(self, text):
        self.label.config(text=f"Status: {text}")

class ControlFrame:
    def __init__(self, parent, toggle_callback):
        self.toggle_button = ttk.Button(parent, text="Iniciar", command=toggle_callback)
        
    def pack(self, **kwargs):
        self.toggle_button.pack(**kwargs)
        
    def update_button_text(self, text):
        self.toggle_button.config(text=text)

class SettingsFrame:
    def __init__(self, parent):
        self.frame = ttk.LabelFrame(parent, text="Configurações", padding=10)
        
        ttk.Label(self.frame, text="Tempo de inatividade (segundos):").pack()
        self.inactive_time = ttk.Entry(self.frame, width=10)
        self.inactive_time.insert(0, "5")
        self.inactive_time.pack()
        
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
        
    def get_inactive_time(self):
        return float(self.inactive_time.get())