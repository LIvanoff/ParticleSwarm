import numpy as np
import random
import os
from PIL import Image

def particle_swarm():
    global_min= [] # глобальный оптимум
    local_min = {} # локальный оптимум всех точек
    particle_dict = {}
    velocity = {}

    for x in range(1,21):
        particle_dict[x] = []
        particle_dict[x] = [random.randint(0, 99) for i in range(2)]
        velocity[x] = []
        velocity[x] = [random.randint(0, 99) for i in range(2)]
        local_min[x] = []
        local_min[x] = particle_dict[x]

    image = load_image('./image.jpg')
    global_min = search_global_min(image,local_min,global_min)

    # for key in particle_dict.keys():
    #     for x in particle_dict[key]:
    #

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
    glob_coor = []

    for key in local_min.keys():
        coordinate = local_min[key]
        x_gl = global_min[0]
        y_gl = global_min[1]
        better = image[coordinate[0]][coordinate[1]].tolist()
        worse = image[x_gl][y_gl].tolist()
        if better < worse:
            print(better)
            print(worse)
            global_min[0] = coordinate[0]
            global_min[1] = coordinate[1]
            glob_coor = better

    # for key in local_min.keys():
    #         if image[local_min[0]][local_min[1]] < image[x_gl][y_gl]:
    #             global_min.append(image[local_min[0]][local_min[1]])
    print('glob = '+str(global_min))
    print(glob_coor)
    return global_min


if __name__ == '__main__':
    particle_swarm()