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
        particle_dict[x].append([random.randint(0, 100) for i in range(2)])
        velocity[x] = []
        velocity[x].append([random.randint(0, 100) for i in range(2)])
        local_min[x] = []
        local_min[x] = particle_dict[x]

    image = load_image('./image.gradient.jpg')
    global_min = search_global_min(image)

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

def search_global_min(image):


    return


if __name__ == '__main__':
    particle_swarm()