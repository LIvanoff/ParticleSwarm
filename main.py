import numpy as np
import random
import os
from PIL import Image

def particle_swarm():
    global_min = [] # глобальный оптимум
    local_min = {} # локальный оптимум всех точек
    particle_dict = {}
    velocity = {}

    for x in range(1,4):
        particle_dict[x] = []
        particle_dict[x] = [random.randint(0, 99) for i in range(2)]
        velocity[x] = []
        velocity[x] = [random.randint(0, 99) for i in range(2)]
        local_min[x] = []
        local_min[x] = particle_dict[x]

    image = load_image('./image/image.jpg')
    global_min = search_global_min(image,local_min,global_min)

    for key in particle_dict.keys():
        x_coordinate = particle_dict[key]
        y_coordinate = local_min[key]
        x = image[x_coordinate[0]][x_coordinate[1]].tolist()
        y = image[y_coordinate[0]][y_coordinate[1]].tolist()
        if x < y:
            local_min[key] = x_coordinate
            g = image[global_min[0]][global_min[1]]
            if y < g:
                global_min[0] = x_coordinate[0]
                global_min[1] = x_coordinate[1]


    print_particle()
    return

def print_particle():
    return

def creat_gif():
    return

def load_image(path : str):
    with Image.open(path) as img:
        image = np.asarray(img)
    return image

def search_global_min(image,local_min,global_min):
    global_min = local_min[1]

    for key in local_min.keys():
        coordinate = local_min[key]
        better = image[coordinate[0]][coordinate[1]].tolist()
        worse = image[global_min[0]][global_min[1]].tolist()
        if better < worse:
            global_min[0] = coordinate[0]
            global_min[1] = coordinate[1]

    return global_min


if __name__ == '__main__':
    particle_swarm()