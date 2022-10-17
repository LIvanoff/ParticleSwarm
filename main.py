import numpy as np
import random
import os
from PIL import Image

def particle_swarm():
    global_min = [] # глобальный оптимум
    local_min = {} # локальный оптимум всех точек
    particle_dict = {}
    velocity = {}

    for x in range(1,30):
        particle_dict[x] = []
        particle_dict[x] = [random.randint(0, 99) for i in range(2)]
        velocity[x] = []
        velocity[x] = [random.randint(0, 1) for i in range(2)]
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
    f = 0
    while (stop_criteria(particle_dict, image)):
        for key in particle_dict.keys():
            alpha = random.randint(0,1)
            beta = random.randint(0,1)

            np_par = np.array(particle_dict[key])
            np_loc = np.array(local_min[key])
            np_vel = np.array(velocity[key])
            np_glo = np.array(global_min)

            velocity[key] = ((np.multiply(alpha,(np_loc-np_par))) + (np.multiply(beta,(np_glo - np_par)))).tolist()
            particle_dict[key] = (np_par + np_vel).tolist() # должно быть ..+1*np_vel[key], но смысла особого в этом нет

            x_coordinate = particle_dict[key]
            y_coordinate = local_min[key]
            x = image[x_coordinate[0]][x_coordinate[1]].tolist()
            y = image[y_coordinate[0]][y_coordinate[1]].tolist()
            if x < y:
                local_min[key] = x_coordinate
                g = image[global_min[0]][global_min[1]].tolist()
                if y < g:
                    global_min[0] = x_coordinate[0]
                    global_min[1] = x_coordinate[1]
            print(str(x))
        f += 1
        print('Итерация: '+str(f))
        print_particle(f, particle_dict)
    return

def print_particle(f, particle_dict):
    img = Image.open('./image/image.jpg')
    for key in particle_dict.keys():
        x_coordinate = particle_dict[key]
        print(str(x_coordinate))
        img.putpixel((x_coordinate[0],x_coordinate[1]), (255,0,0))
    img.save('./result/'+str(f)+'.jpg', quality=100)
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

def stop_criteria(particle_dict, image):
    count = 0
    percent  = 0.0
    for key in particle_dict.keys():
        coordinate = particle_dict[key]
        pos = image[coordinate[0]][coordinate[1]].tolist()
        if pos < [1, 1, 1]:
            count += 1

    percent = count/len(particle_dict)

    if percent < 0.7:
        return True
    else:
        return False

if __name__ == '__main__':
    particle_swarm()