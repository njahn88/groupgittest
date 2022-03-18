import tkinter as tk

window = tk.Tk()

window.attributes('-fullscreen', True)
window.title("Project")

button1 = tk.Button(window, text="Test button")
button1.grid(row=0, column=0)

button2 = tk.Button(window, text="Quit", command =window.destroy)
button2.grid(row=0, column=1)

print("Change")

window.mainloop()