# get x0y0
import numpy as np
import os
import time
import pickle
import matplotlib.pyplot as plt
startTime = time.time()

with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)    
keys = sorted(list(data.keys()))[:-2] # sorts data.dict

keys = [s for s in keys if "1.0" in s]

x0y0_dict = {}

i=0
for key in keys:
    x0y0_dict[i] = (np.asarray(np.unravel_index(data[key].argmax(), data[key].shape)))
    i+=1

keys = [s for s in keys if "1.0" in s]

fig = plt.figure()
ax = fig.add_subplot()
plt.xlabel('x')
plt.ylabel('y')
plt.rcParams["figure.figsize"] = (7,7)
n = np.arange(32)



this = np.ones((2,32))
that = this.T



for i in n:
    this[0],this[1] = x0y0_dict[i][0],x0y0_dict[i][1]

for i in range(32):
    ax.scatter(x0y0_dict[i][0],x0y0_dict[i][1], label = i, color = 'grey')
    
    
for i in n:
    ax.annotate(i,(x0y0_dict[i][0], x0y0_dict[i][1]))
    ax.annotate((x0y0_dict[i][0], x0y0_dict[i][1]),(x0y0_dict[i][0], x0y0_dict[i][1]),xytext=(x0y0_dict[i][0],x0y0_dict[i][1]-7))



        



with open('x0y0.pkl', 'wb') as f:
    pickle.dump(x0y0_dict, f)