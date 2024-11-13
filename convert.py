import json
import random as r
def random_color():
    l=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    color="#"+r.choice(l)+r.choice(l)+r.choice(l)+r.choice(l)+r.choice(l)+r.choice(l)
    return color
def convert_obj_to_custom_format(input_file, output_file,random_c):
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
                    if random_c=="y":
                        lines.append(['color', random_color()])
                    lines.append(['line_3d', [start_vertex, end_vertex]])
    with open(output_file, 'w') as file:
        json.dump(lines, file)
    print(f"Conversion terminée. Le fichier {output_file} a été créé.")
convert_obj_to_custom_format("./obj/"+input("file_name: "), 'model.txt',input("random color (y/n): "))
#btw this file of the code was made by chat-gpt
