import shutil, os, random


img_base_path = 'D:\\Data\\fire_smoke\\fire_smoke\\images'
img_dst = 'D:\\Data\\fire_smoke\\fire_smoke\\images\\test'

l_base_path = 'D:\\Data\\fire_smoke\\fire_smoke\\images\\train'
l_dst = 'D:\\Data\\fire_smoke\\fire_smoke\\labels\\train'


for name in os.listdir(l_base_path):
    if name.split('.')[-1] == 'txt':
        # shutil.move(os.path.join(l_base_path, name), os.path.join(l_dst, name))