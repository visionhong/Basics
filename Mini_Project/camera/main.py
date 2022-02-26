import tkinter as tk
import camera.main_ui as win
import camera.make_widgets as mkw
import camera.camera_service as cs

def main():
    img_path = 'img/a.jpg'
    root = tk.Tk()

    app = win.AppWindow(root, '840x650+100+100', img_path)
    service = cs.CameraService(app)
    mkw.make(app, service)
    app.mainloop()

main()
