'''
Invaders get assassinated hehe. No mo bulletssssss
'''
import tkinter as tk
from abc import ABC, abstractmethod


# My Variables
canvas_width = 800
canvas_height = 600
middle_canvas_width = canvas_width // 2

defender_width = 100
defender_height = 25
middle_defender_width = defender_width // 2

invader_width = 60
invader_height = 30

elevation = 15

invaders = []

class Spaceship(ABC):
    @abstractmethod
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

        self.obj = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
        self.jump = 10


    def move_right(self, event):
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords
        if x2 < canvas_width:
            self.canvas.move(self.obj, self.jump, 0)

    def move_left(self, event):
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords
        if x1 > 0:
            self.canvas.move(self.obj, -self.jump, 0)


class Defender(Spaceship):
    def __init__(self, canvas, x1, y1, x2, y2, color):
        super().__init__(canvas, x1, y1, x2, y2, color)

    def shoot(self, event):
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords
        bullet = self.canvas.create_rectangle(x1+48, 540, x1+52, 560, fill = "yellow")
        
        self.bullet_move(bullet)

    def bullet_move(self, bullet):
        coords_bullet = canvas.coords(bullet)
        Bx1, By1, Bx2, By2 = coords_bullet
        canvas.move(bullet, 0, -self.jump)

        for invader in invaders:
            coords_invader = canvas.coords(invader.obj)
            Ix1, Iy1, Ix2, Iy2 = coords_invader

            if Ix1 <= Bx1 <= Ix2 and Iy1 <= By1 <= Iy2:
                canvas.delete(invader.obj)
                canvas.delete(bullet)

                invaders.remove(invader)
                return

        root.after(15, self.bullet_move, bullet)

    

class Invader(Spaceship):
    def __init__(self, canvas, x1, y1, x2, y2, color):
        super().__init__(canvas, x1, y1, x2, y2, color)


        

# tkinter initialisation
root = tk.Tk()
root.title("Sara's Space Invaders xd")
root.geometry(f"{canvas_width}x{canvas_height}")

# defining canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()


# defenderrr
defender = Defender(
    canvas=canvas,
    x1 = middle_canvas_width - middle_defender_width, 
    y1 = canvas_height - (defender_height + elevation), 
    x2 = middle_canvas_width + middle_defender_width, 
    y2 = canvas_height- elevation,
    color = "green")

# invaders
space_between_inv = 40
invader_count = 6
for i in range(invader_count):
    invader = Invader(
        canvas=canvas,
        x1 = 100 + (space_between_inv // 2) + ((invader_width + space_between_inv)*i)  ,       
        y1 = elevation ,
        x2 = 200 - (space_between_inv // 2) + ((invader_width + space_between_inv)*i) ,        
        y2 = elevation + invader_height,
        color = "white" )
    

    invaders.append(invader)




# key bindings
root.bind("<Right>", defender.move_right)
root.bind("<Left>", defender.move_left)
root.bind("<space>", defender.shoot)

root.mainloop()