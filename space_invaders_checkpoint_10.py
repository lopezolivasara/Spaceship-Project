'''
removed error from checkpoint 9
'''

import tkinter as tk
from abc import ABC, abstractmethod

# My Variables
canvas_width = 800
canvas_height = 600

elevation = 15
spaceship_height = 25
spaceship_width = 60

middle_width, middle_height = canvas_width // 2, canvas_height // 2 

invaders = []
invader_deleted = dict() # if invader_deleted[invader.obj] is 1, then the invader was deleted, otherwise, it was not. 

# Tkinter Initialisation
root = tk.Tk()
root.title("Sara's Space invaders :)")
root.geometry(f"{canvas_width}x{canvas_height}")


class Spaceship(ABC):
    @abstractmethod
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

        self.jump = 10

        self.obj = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)

    def move_left(self, event):
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords
        if x1 > 0:
            canvas.move(self.obj, -self.jump, 0)

    def move_right(self, event):
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords
        if x2 < canvas_width:
            canvas.move(self.obj, self.jump, 0)


class Defender(Spaceship): 
    def __init__(self, canvas, x1, y1, x2, y2, color):
        super().__init__(canvas, x1, y1, x2, y2, color)
    
    def shoot(self, event):   
        coords = canvas.coords(self.obj)
        x1, y1, x2, y2 = coords # coordinates of myself, i.e the defender

        # fuckery to create the initial bullet dynamically
        middle_point = x1 + (x2 - x1) // 2

        print("coordinates of the defender: ", x1, y1, x2, y2, middle_point)

        bullet = canvas.create_rectangle(middle_point - 1, y1-30, middle_point+1, y1, fill="yellow")
        self.bullet_move(bullet)
    
    def bullet_move(self, bullet):
        coords = canvas.coords(bullet)
        x1, y1, x2, y2 = coords
        # make the bullet move
        canvas.move(bullet, 0, -self.jump)

        for invader in invaders: 
            Rx1, Ry1, Rx2, Ry2 = canvas.coords(invader.obj)
            Yx1, Yy1, Yx2, Yy2 = canvas.coords(bullet)

            # collision detection
            if Rx1 <= Yx1 and Yx1 <= Rx2 and Ry1 <= Yy1 and Yy1 <= Ry2: # if this is true, there was a collision
                print("Collision detected!")

                invader_deleted[invader.obj] = 1

                canvas.delete(invader.obj)
                canvas.delete(bullet)

                invaders.remove(invader)
                return

        # run self.bullet_move every 15 miliseconds
        root.after(15, self.bullet_move, bullet)


class Invader(Spaceship):
    def __init__(self, canvas, x1, y1, x2, y2, color):
        super().__init__(canvas, x1, y1, x2, y2, color)

    def move_down(self):
        if (invader_deleted.get(self.obj) != 1):
            print("my obj is ", self.obj)
            coords = canvas.coords(self.obj)
            x1, y1, x2, y2 = coords
            if y2 < canvas_height:
                canvas.move(self.obj, 0, self.jump)

            root.after(1500, self.move_down)


# Defining the canvas
canvas = tk.Canvas(root, height=canvas_height, width=canvas_width, bg="black")
canvas.pack()

# Objects shown on the canvas

# Defender
defender = Defender(
    canvas=canvas, 
    x1=middle_width - spaceship_width, 
    y1=canvas_height - elevation - spaceship_height, 
    x2=middle_width + spaceship_width, 
    y2=canvas_height - elevation, 
    color="green"
    )

# invaders
layers = 3
invader_count = 4
for layer in range(layers):
    for i in range(invader_count):
        invader = Invader(
        canvas=canvas, 
        x1= 20 + (200 * i), 
        y1= (35 * layer) + elevation, 
        x2= 180 + (200 * i), 
        y2= (35 * layer) + elevation + 25, 
        color="red"
        )

        invaders.append(invader)


# Keybindings
root.bind("<Left>", defender.move_left)
root.bind("<Right>", defender.move_right)
root.bind("<space>", defender.shoot)

for invader in invaders:
    invader.move_down()


# Run the app
root.mainloop()
