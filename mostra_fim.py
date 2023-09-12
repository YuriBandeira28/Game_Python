import tkinter as tk
import random
from tkinter import messagebox, Image
from PIL import Image, ImageTk

def show_gif():
    win = tk.Tk()

    label = tk.Label(win)
    label.pack()
    win.geometry('250x250')
    win.title("PERDEU KKKKKKKKKKKKKKKKKKKKKK?")

   
    # Carregar o arquivo GIF com o PIL
    gif = Image.open("end.gif")

    # Converter o GIF para um formato que o Tkinter possa exibir
    frames = []
    for frame in range(0, gif.n_frames):
        gif.seek(frame)
        frames.append(ImageTk.PhotoImage(gif))

    # Função para atualizar o GIF a cada 50ms (20fps)
    def update(ind):
        frame = frames[ind]
        label.configure(image=frame)
        win.after(50, update, (ind+1) % len(frames))
    # Iniciar a animação do GIF
    win.after(0, update, 0)
    win.resizable = False
    win.mainloop()



