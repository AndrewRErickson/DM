### Import Libraries
import numpy as np
import time
import pickle
import pandas as pd
import matplotlib.pyplot as plt
start = time.time()

### Import Data 
voltages = pd.read_excel('DM_Actuator_Values.xlsx')
with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)   
with open('x0y0.pkl', 'rb') as f: 
    x0y0 = pickle.load(f)    
keys = sorted(list(data.keys()))[:-2] # sorts data.dict alphabetically 
keys.remove("03_faltprofil")
keys.remove("04_0.0V_unwrapped.txt")

### Compute z values at every x0y0 for every file in data
act_dict = {}
for i in x0y0:
    value = []
    a= x0y0[i][0]
    b= x0y0[i][1]
    for key in keys:
        value.append(data[key][a,b])
    act_dict[str(a)+str(b)] = value
    
### Plot z at each x0y0 vs actuator voltage
ticks = 11*np.arange(32)
labels = np.arange(32)
counter1 = 0
for i in act_dict.keys():
    plt.figure()
    plt.plot(act_dict[i])
    plt.title("Actuator"+str(counter1))
    for i in ticks:
        plt.axvline(x = i, color = 'grey')
    plt.xticks(ticks=ticks, labels=labels, rotation = -90)
    plt.ylim(500,3000)
    plt.xlabel("Actuator")
    plt.ylabel("height")
    plt.savefig("flat_values/Actuator"+str(counter1))
    counter1+=1

### Run Time
print("time in seconds: " + str(time.time()-start))