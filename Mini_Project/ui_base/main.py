import ui_base.fileRW as f
import ui_base.main_ui as ui
import tkinter as tk

def main():
    root = tk.Tk()
    file = f.FileRW('../ui')
    app = ui.AppWindow(root, '650x500+100+100', file)
    app.mainloop()

main()