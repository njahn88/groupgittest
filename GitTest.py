from tkinter import *
import tkinter as tk
from tkinter.ttk import *

#function to set up the window and buttons
def windowSetUp():

    window.geometry(f"{800}x{600}")
    window.title("Project")

#class for the player character (shape, speed, etc...)
class player:

    def __init__(self, window = None):
        self.x = 0
        self.y = 0
        self.canvas = Canvas(window)

        self.rectangle = self.canvas.create_rectangle(5, 5, 25, 25, fill = "black")

        self.canvas.pack()

        self.movement()

    def movement(self):
        self.canvas.move(self.rectangle, self.x, self.y)

        self.canvas.after(100, self.movement)

    def left(self, e):
        print(e.keysym)
        self.x = -5
        self.y = 0

    def right(self, e):
        print(e.keysym)
        self.x = 5
        self.y = 0

    def up(self, e):
        print(e.keysym)
        self.x = 0
        self.y = -5

    def down(self, e):
        print(e.keysym)
        self.x = 0
        self.y = 5

#sets up the keybinds (arrow keys)
def keySetup():
    window.bind("<KeyPress-Left>", lambda e: playerChar.left(e))
    window.bind("<KeyPress-Right>", lambda e: playerChar.right(e))
    window.bind("<KeyPress-Up>", lambda e: playerChar.up(e))
    window.bind("<KeyPress-Down>", lambda e: playerChar.down(e))


window = tk.Tk()
playerChar = player(window)
keySetup()

windowSetUp()
        
window.mainloop()