'''
In this file, we defined the defender, but only using basic arithmetic and no magic numbers. 
'''

import tkinter as tk
from abc import ABC, abstractmethod

root = tk.Tk()

root.title("Sara's Space Invaders :)")

canvas_width = 800
canvas_height = 600

elevation = 15
spaceship_height = 25
spaceship_width = 60

middle_width, middle_height = canvas_width // 2, canvas_height // 2 

root.geometry(f"{canvas_width}x{canvas_height}")

canvas = tk.Canvas(root, height=canvas_height, width=canvas_width, bg="black")
canvas.pack()

spaceship = canvas.create_rectangle(middle_width - spaceship_width, canvas_height - elevation - spaceship_height, middle_width + spaceship_width, canvas_height - elevation, fill="green")


root.mainloop()