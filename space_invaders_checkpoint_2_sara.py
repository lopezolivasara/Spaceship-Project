'''
defender is inside a class now. i hate self.
'''

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
middle_canvas_width = canvas_width // 2

defender_width = 100
defender_height = 25
middle_defender_width = defender_width // 2

elevation = 15

# tkinter initialisation
root = tk.Tk()
root.title("Sara's Space Invaders xd")
root.geometry(f"{canvas_width}x{canvas_height}")

# defining canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()


#defenderrr
defender = Spaceship(
    canvas=canvas,
    x1 = middle_canvas_width - middle_defender_width, 
    y1 = canvas_height - (defender_height + elevation), 
    x2 = middle_canvas_width + middle_defender_width, 
    y2 = canvas_height- elevation,
    color = "green")




root.mainloop()