from abc import ABC, abstractmethod
import tkinter as tk
import time, math

class Spaceship(ABC):
    def __init__(self, canvas, x,y, width=50, height=30, color="red", speed=10, health=1):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.health = health
        self.bullets = []

        self.id = self.canvas.create_rectangle(x,y,x+width, y+height, fill=color)

    def move_left(self):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x1 > 0:
            self.canvas.move(self.id, -self.speed, 0)

    def move_right(self):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if x1 > 0:
            self.canvas.move(self.id, -self.speed, 0)

    abstractmethod
    def shoot(self):
        pass

    def update_bullets(self):
        for b in self.bullets:
            bullet.move()

        self.bullets = [b for b in self.bullets if b.active]


class Defender(Spaceship):
    def __init__(self, canvas):
        super().__init__(canvas, 350, 550, width=100, color="red")

    def shoot(self):
        print("defender: shoot")


class Invader_level1(Spaceship):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y, width=75, color="blue")

    def shoot(self):
        pass
        print("invader: shoot")


class Bullet (ABC):
    def __init__(self, spaceship, speed=10, damage=1, color="yellow"):
        self.canvas = spaceship.canvas
        self.speed = speed
        self.damage = damage
        self.active = True

        x1,y1,x2,y2 = self.canvas.coords(spaceship)
        self.id = self.canvas.create_rectangle(
            x1 + (spaceship.width / 3)-2,
            y1-10,
            x1 + (spaceship.width / 3)+2,
            y1,
            fill=color
        )
        spaceship.bullets.append(self.id)

    def move_self():
        pass


class GameApp:
    def __init__(self):
        self.game_update()
        pass

    def game_update(self):
        root.after(30, self.game_update)

    def run(self):
        root.mainloop()

        


root = tk.Tk()
root.geometry("800x600")
canvas = tk.Canvas(root, height=800, width=600, bg="black")
canvas.pack()

#x1 = Spaceship(canvas, 350, 550, width=100)
defender = Defender(canvas)
invaders = []

for row in range(1,3):
    for column in range(1,5):
        #x2 = Spaceship(canvas, column*100, row*70, color="blue")
        invaders.append(Invader_level1(canvas, column*100, row*70))

def tmp_left(event):
    for i in invaders:
        i.move_left()

def tmp_shoot(event):
    b = Bullet(defender)

root.bind("<Left>", tmp_left)
root.bind("x", tmp_shoot)





root.mainloop()

# added a comment to invaders.py