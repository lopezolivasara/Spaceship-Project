import tkinter as tk
from abc import ABC, abstractmethod

# My Variables
canvas_width = 800
canvas_height = 600

elevation = 15
spaceship_height = 25
spaceship_width = 60

middle_width, middle_height = canvas_width // 2, canvas_height // 2 

class Spaceship():
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

        self.jump = -10

        self.obj = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)

    def move_left(self, event):
        coords = canvas.coords(self.obj)
        canvas.move(self.obj, -self.jump, 0)

    def move_right(self, event):
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords
        if x2 < canvas_width:
            canvas.move(self.obj, self.jump, 0)


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

# Keybindings
root.bind("<Left>", defender.move_left)
root.bind("<Right>", defender.move_right)

# Run the app
root.mainloop()
