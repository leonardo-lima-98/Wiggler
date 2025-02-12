# main.py
from src.gui.app_window import MouseMoverApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
