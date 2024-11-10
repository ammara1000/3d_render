from turtle import *
import random
import time
from math import *
import json
def convert_obj_to_custom_format(input_file, output_file):
    vertices = []
    lines = []
    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            elif line.startswith('v '):
                vertex = line.split()[1:]
                vertices.append(tuple(map(float, vertex)))
            elif line.startswith('f '):
                face = line.split()[1:]
                indices = [int(part.split('/')[0]) - 1 for part in face]
                for i in range(len(indices)):
                    start_vertex = vertices[indices[i]]
                    end_vertex = vertices[indices[(i + 1) % len(indices)]]
                    lines.append(['line_3d', [start_vertex, end_vertex]])
    with open(output_file, 'w') as file:
        json.dump(lines, file)
convert_obj_to_custom_format(input("file_name: "), 'model.txt')
ht()
w=0.5
width(w)
speed(0)
def dot_(coords):
    up()
    goto(coords)
    down()
    dot(w)
def dot_3d_(coords):
    up()
    goto(dot_3d(rot_3d((coords),rot),focal_point,proj))
    down()
    dot(w)
def line(coords):
    up()
    goto(coords[0])
    down()
    goto(coords[1])
def line_3d(coords):
    up()
    goto(dot_3d(rot_3d((coords[0]),rot),focal_point,proj))
    down()
    goto(dot_3d(rot_3d((coords[1]),rot),focal_point,proj))
def polygone(coords):
    up()
    goto(coords[0])
    down()
    for i in coords:
        goto(i)
def polygone_3d(coords):
    up()
    goto(dot_3d(rot_3d((coords[0]),rot),focal_point,proj))
    down()
    for i in coords:
        goto(dot_3d(rot_3d((i),rot),focal_point,proj))
def r():
    return (random.randint(-150,150),random.randint(-150,150))
def r_3d():
    return (random.randint(-150,150),random.randint(-150,150),random.randint(-150,150))

def dot_3d(coords_3d,focal_point,proj=1.5):
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
    for i in shape:
        if i[0]=="line":
            line(i[1])
        elif i[0]=="color":
            color(i[1])
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
            width(w)
        elif i[0]=="start_fill":
            fillcolor(i[1])
            begin_fill()
        elif i[0]=="end_fill":
            end_fill()
focal_point=-5#---------------------------
proj=1000#-----------------------------------
rot=(20,0,180)#--------------------------------
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
        for i in range(0,360,20):
            global rot
            global focal_point
            global proj
            rot=(rot[0],i+1,180)
            shape=F5_shape(focal_point,proj,rot)
            render(shape)
            time.sleep(0.5)
            clear()
rotate_shape()
#render(shape)
done()