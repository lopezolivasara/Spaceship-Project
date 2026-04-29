'''
defined defender with basic arithmetic and no magic numbers... again
'''

import tkinter as tk

root = tk.Tk()


root.title("Sara's Space Invaders xd")

canvas_width = 800
canvas_height = 600
middle_canvas_width = canvas_width // 2

defender_width = 100
defender_height = 25
middle_defender_width = defender_width // 2

elevation = 15

root.geometry(f"{canvas_width}x{canvas_height}")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

defender = canvas.create_rectangle(
    middle_canvas_width - middle_defender_width, 
    canvas_height - (defender_height + elevation), 
    middle_canvas_width + middle_defender_width, 
    canvas_height- elevation,
    fill = "green")

root.mainloop()




