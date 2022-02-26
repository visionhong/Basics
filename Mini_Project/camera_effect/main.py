import tkinter as tk
import camera_effect.main_ui as win
import camera_effect.make_widgets as mkw
import camera_effect.camera_service as cs

def main():
    img_path = 'img/camera.jpg'
    root = tk.Tk()

    app = win.AppWindow(root, '840x650+100+100', img_path)
    service = cs.CameraService(app)
    mkw.make(app, service)
    app.mainloop()

main()
