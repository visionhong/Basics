
import parking_system.main_ui as ui
import tkinter

def main():
    window = tkinter.Tk()
    title = "parking system"
    geometry = ("1000x540+100+100")
    app = ui.AppWindow(window, title, geometry)
    app.mainloop()

main()