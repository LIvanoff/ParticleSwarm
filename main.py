import numpy as np
import random
import os
from PIL import Image

def particle_swarm():
    global_min = [] # глобальный оптимум
    local_min = {} # локальный оптимум
    particle_dict = {} # координаты частиц
    velocity = {} # скорость частиц

    for x in range(1,190): # инициализация координат частиц
        particle_dict[x] = []
        particle_dict[x] = [random.randint(0, 199) for i in range(2)]
        velocity[x] = []
        velocity[x] = [random.randint(-1,1) for i in range(2)]
        local_min[x] = []
        local_min[x] = particle_dict[x]

    image = load_image('./image/image5.jpg')
    global_min = search_global_min(image,local_min,global_min) # инициализация глобального оптимума

    for key in particle_dict.keys(): # поиск лок минимума каждой частицы и глоб минимума
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
    while (stop_criteria(particle_dict, image)): # изменение скоростей и координат частиц
        for key in particle_dict.keys():
            alpha = random.randint(0,1)
            beta = random.randint(0,1)

            np_par = np.array(particle_dict[key])
            np_loc = np.array(local_min[key])
            np_vel = np.array(velocity[key])
            np_glo = np.array(global_min)

            velocity[key] = ((np.multiply(alpha,(np_loc-np_par))) + (np.multiply(beta,(np_glo - np_par)))).tolist() #''''''
            particle_dict[key] = (np_par + np_vel).tolist() # должно быть ..+(np.multiply1*np_vel[key]), но смысла особого в этом нет

            x_coordinate = particle_dict[key]
            y_coordinate = local_min[key]

            x = [255, 255, 255]
            #print('x_coordinate '+str(x_coordinate))

            if ((x_coordinate[0] <= 199) & (x_coordinate[1] <= 199)) & ((x_coordinate[0] >=0) & (x_coordinate[1] >=0)):
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
    creat_gif()
    return

def print_particle(f, particle_dict):
    img = Image.open('./image/image5.jpg')
    for key in particle_dict.keys():
        x_coordinate = particle_dict[key]
        #print('print '+str(x_coordinate))

        if ((x_coordinate[0] <= 199) & (x_coordinate[1] <= 199)) & ((x_coordinate[0] >=0) & (x_coordinate[1] >=0)):
            img.putpixel((x_coordinate[0],x_coordinate[1]), (255,0,0))

    img.save('./result/new_result/'+str(f)+'.jpg', quality=100)
    return

def creat_gif():
    frames = []
    name_list = os.listdir('./result/new_result')

    for frame_number in name_list:
        # Открываем изображение каждого кадра.
        frame = Image.open('./result/new_result/'+str(frame_number))
        # Добавляем кадр в список с кадрами.
        frames.append(frame)
    # Берем первый кадр и в него добавляем оставшееся кадры.
    frames[0].save(
        './result/new_result/result.gif',
        save_all=True,
        append_images=frames[1:],  # Срез который игнорирует первый кадр.
        optimize=True,
        duration=1000,
        loop=0)

    return

def load_image(path : str):
    with Image.open(path) as img:
        image = np.asarray(img)
    return image

def search_global_min(image,local_min,global_min): # поиск глоб минимума для инициализации
    global_min = local_min[1]

    for key in local_min.keys():
        coordinate = local_min[key]
        better = image[coordinate[0]][coordinate[1]].tolist()
        worse = image[global_min[0]][global_min[1]].tolist()
        if better < worse:
            global_min[0] = coordinate[0]
            global_min[1] = coordinate[1]

    return global_min

def stop_criteria(particle_dict, image): # критерий остановы
    count = 0.0
    percent  = 0.0
    color = [255,255,255]

    for key in particle_dict.keys():
        coordinate = particle_dict[key]
        if ((coordinate[0] <= 199) & (coordinate[1] <= 199)) & ((coordinate[0] >= 0) & (coordinate[1] >= 0)):
            color = image[coordinate[0]][coordinate[1]].tolist()

        if color == [0, 0, 0]:
            count += 1

    if count != 0:
        percent = count / len(particle_dict)

    if percent < 0.9:
        return True
    else:
        return False

if __name__ == '__main__':
    particle_swarm()