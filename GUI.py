import tkinter as tk

x1 = y1 = None

def start_rectangle(event):
    global x1,y1
    x1 = event.x
    y1 = event.y

def finish_rectangle(event):
    canvas.create_rectangle(x1, y1, event.x,event.y)
    #if x1 == None:
        #x1 = event.x
        #y1 = event.y
    #else: 
        #canvas.create_rectangle(x1, y1, event.x,event.y)
        #x1 = y1 = None

def print_xy(event):
    print("clicked", event)
    pass

tmp_rectangle = None
def draw_rectangle(event):
    global tmp_rectangle
    if tmp_rectangle != None:
        canvas.delete(tmp_rectangle)
        tmp_rectangle = None
    tmp_rectangle = canvas.create_rectangle(x1, y1, event.x,event.y)

root = tk.Tk()

root.title("title")
root.geometry("800x600")

canvas = tk.Canvas(root, height=600, width=800, bg="white")
canvas.pack()

root.bind("<Button-1>", start_rectangle)
canvas.bind('<B1-Motion>', draw_rectangle)
canvas.bind('<ButtonRelease-1>', finish_rectangle)

root.mainloop()




exit(0)

import tkinter as tk

def hello(event=None):
    my_name = my_input.get()
    #print(f"Hello, {my_name}")
    my_label.config(text=f"Hello, {my_name}")

root = tk.Tk()

root.title("title")
root.geometry("800x600")

my_input = tk.Entry()
my_input.pack()

my_button = tk.Button(text="Greet", command=hello)
my_button.pack()

my_label = tk.Label(text="", bg="yellow")
my_label.pack()

root.bind("<Enter>", hello)


root.mainloop()




exit(0)




import tkinter as tk

def move_left(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    print("left:", x1)
    if x1 > 0:
        canvas.move(spaceship, -10, 0)
    
def move_right(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    print("right:", x2)
    if x2 < 800:
        canvas.move(spaceship, 10, 0)

'''def move_up(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    print("up:", y1)
    if y1 > 0:
        canvas.move(spaceship, 0, -10)

def move_down(event):
    coords = canvas.coords(spaceship)
    x1, y1, x2, y2 = coords
    print("down:", y2)
    if y2 < 600:
        canvas.move(spaceship, 0, 10)'''


root= tk.Tk()

root.title("My first GUI")
root. geometry("800x600")
#root.resizabe
#root.configure


canvas = tk.Canvas(root, width=800, height=600, bg="lightgray")
canvas.pack()

spaceship = canvas.create_rectangle(400,500,550,550, fill="red", outline="black")

root.bind("<Right>", move_right)
root.bind("<Left>", move_left)
'''root.bind("<Up>", move_up)
root.bind("<Down>", move_down)'''


root.mainloop()


exit(0)




from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()



import tkinter as tk

def hello():
    print("hello")
    exit()

root = tk.Tk()

root.title("title")
root.geometry("800x600")

my_button = tk.Button(text="something", command=hello)
my_button.pack()


root.mainloop()


#import tkinter as tk
#root = tk.Tk()
#root.title("Grid Example")

#Create three labels
#label1 = tk.Label(root, text = "Label 1")
#label2 = tk.Label(root, text = "Label 2")
#label3 = tk.Label(root, text = "Label 3")

#Grid the labels in a 2x2 grid
#label1.grid(row=0, columns=0)
#label2.grid(row=0, columns=1)
#label3.grid(row=1, columns=0, columnspan=2)

#root.mainloop()



import tkinter as tk

root = tk.Tk()

root.title("title")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

top_bar = canvas.create_rectangle(0,0,800,50, fill="red")

green_center_area = canvas.create_rectangle(300,200,500,400, fill="green")

bottom_bar = canvas.create_rectangle(0,600,800,550, fill="blue")

# comment added by shaf
