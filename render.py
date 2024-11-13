import turtle
import random
import time
from math import *
import json
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("3d render")
root.geometry("800x600")
root.configure(bg="black")
canvas_frame = ttk.Frame(root)
canvas_frame.grid(row=0, column=0, sticky="nsew")
canvas = turtle.ScrolledCanvas(canvas_frame, width=600, height=600)
canvas.pack(fill="both", expand=True)
debug_frame = ttk.Frame(root, width=200)
debug_frame.grid(row=0, column=1, sticky="nsew")
debug_text = tk.Text(debug_frame, wrap="word", state="disabled", width=30, bg="black", fg="#00EE00")
debug_text.pack(fill="both", expand=True)
input_text = tk.Entry(debug_frame, width=30, bg="black", font=("Courier", 12), fg="#00EE00")
input_text.pack(fill="x", pady=10)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
t = turtle.RawTurtle(screen)
def debug(message):
    debug_text.config(state="normal")
    debug_text.insert("end", message + "\n")
    debug_text.config(state="disabled")
    debug_text.see("end")
def submit_input():
    user_input = input_text.get()
    with open("key.txt", 'w') as log_file:
            log_file.write(user_input)
    input_text.delete(0, 'end')
submit_button = ttk.Button(debug_frame, text="Envoyer", command=submit_input)
submit_button.pack(pady=5)
def look_key():
    global key
    with open('key.txt', 'r') as file:
        key = file.readline().strip()
        if key!="":
            debug(key)
def clear_key():
    with open("key.txt", "w") as file:
        pass
var=10
def run_key():
    look_key()
    global focal_point
    global rot
    global pos
    global var
    if key=="haut":
        rot=(rot[0]-var,rot[1],rot[2])
    if key=="bas":
        rot=(rot[0]+var,rot[1],rot[2])
    if key=="droite":
        rot=(rot[0],rot[1]+var,rot[2])
    if key=="gauche":
        rot=(rot[0],rot[1]-var,rot[2])
    if key=="o":
        rot=(rot[0],rot[1],rot[2]+var)
    if key=="p":
        rot=(rot[0],rot[1],rot[2]-var)
    if key=="space":
        pos=(pos[0],pos[1]+var,pos[2])
    if key=="maj":
        pos=(pos[0],pos[1]-var,pos[2])
    if key=="w":
        focal_point+=-var
    if key=="s":
        focal_point+=var
    if key=="r":
        screen.update()
        root.update()
    if key=="1":
        var=1
    if key=="2":
        var=5
    if key=="3":
        var=10
    if key=="4":
        var=50
    if key=="5":
        var=100
    if key=="6":
        var=500
    if key=="esc":
        clear_key()
        1/0,"var:",var
    clear_key()
    if key != "":
        debug(str(focal_point)+" rot:"+str(rot)+" pos:"+str(pos)+" var:"+str(var))
    if key in ["haut","bas","gauche","droite","o","p","space","maj","w","s"]:
        return "skip"
t.ht()
t.color("#880000")
w=0.5
t.width(w)
t.speed(0)
def dot_(coords):
    t.up()
    t.goto(coords)
    t.down()
    t.dot(w)
def dot_3d_(coords):
    t.up()
    t.goto(dot_3d(rot_3d((coords),rot),focal_point,proj))
    t.down()
    t.dot(w)
def line(coords):
    t.up()
    t.goto(coords[0])
    t.down()
    t.goto(coords[1])
def line_3d(coords):
    t.up()
    t.goto(dot_3d(rot_3d((coords[0]),rot),focal_point,proj))
    t.down()
    t.goto(dot_3d(rot_3d((coords[1]),rot),focal_point,proj))
    t.dot(0.0001)
def polygone(coords):
    t.up()
    t.goto(coords[0])
    t.down()
    for i in coords:
        t.goto(i)
def polygone_3d(coords):
    t.up()
    t.goto(dot_3d(rot_3d((coords[0]),rot),focal_point,proj))
    t.down()
    for i in coords:
        t.goto(dot_3d(rot_3d((i),rot),focal_point,proj))
        t.dot(0.0001)
def space_plan(func,step,size):
    data=[]
    for i in range(-size,size):
        temp_data=[]
        for j in range(-size,size):
            x=step*i
            y=step*j
            z=eval(func+"(x,y,step)")
            temp_data.append([x,y,z])
        data.append(temp_data)      
    for i in range(1,(2*size)-1):
        for j in range(2*size):
            if data[i-1][j][2]!=None and data[i][j][2]!=None:
                line_3d([data[i-1][j],data[i][j]])
            if data[j][i-1][2]!=None and data[j][i][2]!=None:
                line_3d([data[j][i-1],data[j][i]])
def r():
    return (random.randint(-150,150),random.randint(-150,150))
def r_3d():
    return (random.randint(-150,150),random.randint(-150,150),random.randint(-150,150))

def dot_3d(coords_3d,focal_point,proj=1.5):
    coords_3d=(pos[0]+coords_3d[0],pos[1]+coords_3d[1],pos[2]+coords_3d[2])
    if coords_3d[2]==focal_point:
        focal_point+=1
    coef=-(proj/(coords_3d[2]-focal_point))
    coords_2d=(coords_3d[0]*coef,coords_3d[1]*coef)
    return coords_2d
def rot_2d(coords,rot):
    t=radians(rot)
    x=coords[0]*cos(t)-coords[1]*sin(t)
    y=coords[0]*sin(t)+coords[1]*cos(t)
    return (x,y)
def rot_3d(coords, rot):
    rotx, roty, rotz = rot
    rotx = radians(rotx)
    roty = radians(roty)
    rotz = radians(rotz)
    x, y, z = coords
    y1 = y * cos(rotx) - z *sin(rotx)
    z1 = y * sin(rotx) + z * cos(rotx)
    x1 = x
    x2 = x1 * cos(roty) + z1 * sin(roty)
    z2 = -x1 * sin(roty) + z1 * cos(roty)
    y2 = y1
    x3 = x2 * cos(rotz) - y2 * sin(rotz)
    y3 = x2 * sin(rotz) + y2 * cos(rotz)
    z3 = z2
    return (x3, y3, z3)
def render(shape):
    global w
    global rot
    for i in shape:
        if i[0]=="line":
            line(i[1])
        elif i[0]=="color":
            t.color(i[1])
        elif i[0]=="polygone":
            polygone(i[1])
        elif i[0]=="dot":
            dot_(i[1])
        elif i[0]=="polygone_3d":
            polygone_3d(i[1])
        elif i[0]=="dot_3d":
            dot_3d_(i[1])
        elif i[0]=="line_3d":
            line_3d(i[1])
        elif i[0]=="width":
            w=i[1],
            t.width(w)
        elif i[0]=="start_fill":
            t.fillcolor(i[1])
            t.begin_fill()
        elif i[0]=="end_fill":
            t.end_fill()
        elif i[0]=="plan":
            space_plan(i[1][0],i[1][1],i[1][2])
        elif i[0]=="rot":
            rot=i[1]
focal_point=750#---------------------------
proj=1500#-----------------------------------
rot=(0,0,0)#--------------------------------
pos=(0,0,0)#------------------------------
def plan_def(x,y,step):
    c=0
    a=complex(x,0)
    b=complex(0,y)
    z_=(e**(a))*(e**(b))
    z=z_.real
    if z.imag < c-step and z.imag >= c+step:
        return z
    else:
        return None
def plan_0(x,y,step):
    z=0
    return z
def F5_shape(focal_point,proj,rot):
    #shape=[
    #    ["color", "blue"],
    #    ["polygone_3d",[(-100,-100,-100),(-100,-100,100),(100,-100,100),(100,-100,-100),(-100,-100,-100)]],
    #    ["polygone_3d",[(-100,100,-100),(-100,100,100),(100,100,100),(100,100,-100),(-100,100,-100)]],
    #    ["line_3d",[(-100,-100,-100),(-100,100,-100)]],
    #    ["line_3d",[(-100,-100,100),(-100,100,100)]],
    #    ["line_3d",[(100,-100,100),(100,100,100)]],
    #    ["line_3d",[(100,-100,-100),(100,100,-100)]]
    #]
    with open('model.txt', 'r') as file:
        line_ = file.readline().strip()
    shape=json.loads(line_)
    return shape
shape=F5_shape(focal_point,proj,rot)
def rotate_shape():
    while True:
        screen.bgcolor("#000000")
        shape=F5_shape(focal_point,proj,rot)
        screen.tracer(0)
        render(shape)
        screen.update()
        root.update()
        debug("done")
        while True:
            skip=run_key()
            root.update()
            if skip=="skip":
                break
        screen.clear()
        screen.bgcolor("#000000")
rotate_shape()
#render(shape)
debug("done")
turtle.done()
