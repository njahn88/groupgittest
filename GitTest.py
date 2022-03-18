import tkinter as tk
from turtle import width

window = tk.Tk()

window.geometry(f"{800}x{600}")
window.title("Project")

button1 = tk.Button(window, text="Test button")
button1.grid(row=0, column=0)

button2 = tk.Button(window, text="Quit", command =window.destroy)
button2.grid(row=0, column=1)


window.mainloop()