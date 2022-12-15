import numpy as np
import pickle
import matplotlib.pyplot as plt
a = np.array((None,0, 1,2,3,None))
b =np.arange(4,28,1)
c = np.array((None,28,29,30,31,None))
d=np.concatenate((a,b,c), axis=None)
DM = np.reshape(d, (6,6))

with open('DM.pkl', 'wb') as f:
    pickle.dump(DM, f)
    

e = np.where(DM==19)
et = e[0]-1,e[1]
eb = e[0]+1,e[1]
el = e[0],e[1]-1
er = e[0],e[1]+1
etl = e[0]-1,e[1]-1
etr = e[0]-1,e[1]+1
ebl = e[0]+1,e[1]-1
ebr = e[0]+1,e[1]+1
actu = 19

loc = np.where(DM==actu)
neighbors = {
    "actuator" : actu,
    "top" : int(DM[loc[0]-1,loc[1]]),
    "bottom" : int(DM[loc[0]+1,loc[1]]),
    "left" : int(DM[loc[0],loc[1]-1]),
    "right" : int(DM[loc[0],loc[1]+1]),
    "topleft" : int(DM[loc[0]-1,loc[1]-1]),
    "topright" : int(DM[loc[0]-1,loc[1]+1]),
    "bottomleft" : int(DM[loc[0]+1,loc[1]-1]),
    "bottomright" : int(DM[loc[0]+1,loc[1]+1]),
    }





t = int(DM[loc[0]-1,loc[1]])
b = int(DM[loc[0]+1,loc[1]])
l = int(DM[loc[0],loc[1]-1])
r = int(DM[loc[0],loc[1]+1])
tl = int(DM[loc[0]-1,loc[1]-1])
tr = int(DM[loc[0]-1,loc[1]+1])
bl = int(DM[loc[0]+1,loc[1]-1])
br = int(DM[loc[0]+1,loc[1]+1])


print(DM)
print(DM[e])
print(DM[et])
print(DM[eb])
print(DM[el])
print(DM[er])
print(DM[etl],DM[etr],DM[ebl],DM[ebr])
