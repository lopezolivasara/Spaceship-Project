import tkinter as tk
from abc import ABC, abstractmethod

class Spaceship():
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

        self.obj = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)



# My Variables
canvas_width = 800
canvas_height = 600

elevation = 15
spaceship_height = 25
spaceship_width = 60

middle_width, middle_height = canvas_width // 2, canvas_height // 2 

# Tkinter Initialisation
root = tk.Tk()
root.title("Sara's Space Invaders :)")
root.geometry(f"{canvas_width}x{canvas_height}")

# Defining the canvas
canvas = tk.Canvas(root, height=canvas_height, width=canvas_width, bg="black")
canvas.pack()

# Objects shown on the canvas

defender = Spaceship(
    canvas=canvas, 
    x1=middle_width - spaceship_width, 
    y1=canvas_height - elevation - spaceship_height, 
    x2=middle_width + spaceship_width, 
    y2=canvas_height - elevation, 
    color="green"
    )

# Run the app
root.mainloop()