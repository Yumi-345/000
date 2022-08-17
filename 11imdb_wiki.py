__Author__ = "yumi"


from scipy.io import loadmat
import pandas as pd
import numpy as np
pd.set_option('display.width', None)

m = loadmat("wiki.mat")
names = ['dob', 'photo_taken', 'full_path', 'gender', 'name', 'face_location', 'face_score', 'second_face_score']
data = pd.DataFrame(columns=names)

data[names[0]] = m['wiki'][0][names[0]][0][0]
data[names[1]] = m['wiki'][0][names[1]][0][0]
data[names[2]] = [i for innerlist in m['wiki'][0][names[2]][0][0] for i in innerlist]
data[names[3]] = m['wiki'][0][names[3]][0][0]
data[names[4]] = m['wiki'][0][names[4]][0][0]
data[names[5]] = [list(i) for innerlist in m['wiki'][0][names[5]][0][0] for i in innerlist]
data[names[6]] = m['wiki'][0][names[6]][0][0]
data[names[7]] = m['wiki'][0][names[7]][0][0]

print(data.head())
data.to_csv("./wiki.csv")

