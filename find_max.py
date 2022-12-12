### Import Libraries
import numpy as np
import time
import pickle
import matplotlib.pyplot as plt
startTime = time.time()

### Import Data 
with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)    
keys = sorted(list(data.keys()))[:-2] # sorts data.dict alphabetically 
keys = [s for s in keys if "1.0" in s] # removes all data except for 1.0V

### Calculate x0y0 Positions
x0y0_dict = {} # Dictionary to store x0y0 positions
i=31
for key in keys:
    x0y0_dict[i] =np.flip((np.asarray(np.unravel_index(data[key].argmax(), 
                    data[key].shape))))
    i-=1

### Create plot of x0y0 positions for each actuator
fig = plt.figure()
ax = fig.add_subplot()
plt.xlabel('x')
plt.ylabel('y')
plt.rcParams["figure.figsize"] = (7,7)
for i in range(32):
    ax.scatter(x0y0_dict[i][0],x0y0_dict[i][1], label = i, color = 'grey')
    ax.annotate(i,(x0y0_dict[i][0], x0y0_dict[i][1]))
    ax.annotate((x0y0_dict[i][0], x0y0_dict[i][1]),(x0y0_dict[i][0], 
        x0y0_dict[i][1]),xytext=(x0y0_dict[i][0],x0y0_dict[i][1]-7))

### Save x0y0_dict 
with open('x0y0.pkl', 'wb') as f:
    pickle.dump(x0y0_dict, f)

### Run Time
print("time in seconds: " + str(time.time()-startTime))