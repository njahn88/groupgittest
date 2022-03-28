from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image


window = tk.Tk()


window.geometry(f"{800}x{600}")
window.title("Main Menu")
window.configure(bg = "#0B0B45")

img = Image.open("wyly_level_9.png")
new_img = img.resize((300,500))

img = ImageTk.PhotoImage(new_img)


label = tk.Label(window, image = img)
label.place(x = 0, y = 100)

def buttonSetUp():

    levelOne = tk.Button(window, text = "Level 1", height = 2, width = 10, bg = "#ADD8E6" )
    levelOne.place(x = 350, y = 100)
    
    levelTwo = tk.Button(window, text = "Level 2", height = 2, width = 10, bg = "#ADD8E6" ) 
    levelTwo.place(x = 500, y = 100)

    levelThree = tk.Button(window, text = "Level 3", height = 2, width = 10, bg = "#ADD8E6" ) 
    levelThree.place(x = 650, y = 100)

    levelFour = tk.Button(window, text = "Level 4", height = 2, width = 10, bg = "#ADD8E6" )
    levelFour.place(x = 350, y = 175)

    levelFive = tk.Button(window, text = "Level 5", height = 2, width = 10, bg = "#ADD8E6" )
    levelFive.place(x = 500, y = 175)

    levelSix = tk.Button(window, text = "Level 6", height = 2, width = 10, bg = "#ADD8E6" )
    levelSix.place(x = 650, y = 175)

    levelSeven = tk.Button(window, text = "Level 7", height = 2, width = 10, bg = "#ADD8E6" )
    levelSeven.place(x = 350, y = 250)

    levelEight = tk.Button(window, text = "Level 8", height = 2, width = 10, bg = "#ADD8E6" )
    levelEight.place(x = 500, y = 250)

    levelNine = tk.Button(window, text = "Level 9", height = 2, width = 10, bg = "#ADD8E6" )
    levelNine.place(x = 650, y = 250)

    levelTen = tk.Button(window, text = "Level 10", height = 2, width = 10, bg = "#ADD8E6" )
    levelTen.place(x = 350, y = 325)

    levelEleven = tk.Button(window, text = "Level 11", height = 2, width = 10, bg = "#ADD8E6" )
    levelEleven.place(x = 500, y = 325)

    levelTwelve = tk.Button(window, text = "Level 12", height = 2, width = 10, bg = "#ADD8E6" )
    levelTwelve.place(x = 650, y = 325)

    levelThirteen = tk.Button(window, text = "Level 13", height = 2, width = 10, bg = "#ADD8E6" )
    levelThirteen.place(x = 350, y = 400)

    levelFourteen = tk.Button(window, text = "Level 14", height = 2, width = 10, bg = "#ADD8E6" )
    levelFourteen.place(x = 500, y = 400)

    levelFifteen = tk.Button(window, text = "Level 15", height = 2, width = 10, bg = "#ADD8E6" )
    levelFifteen.place(x = 650, y = 400)

    levelSixteen = tk.Button(window, text = "Level 16", height = 2, width = 10, bg = "#ADD8E6" )
    levelSixteen.place(x = 500, y = 475)



buttonSetUp()
        
window.mainloop()