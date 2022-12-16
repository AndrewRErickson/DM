from sklearn import metrics
import numpy as np
import time
import pickle
from lmfit import Model
import pandas as pd
import matplotlib.pyplot as plt
start = time.time()

### Import Data 
voltages = np.asarray(pd.read_excel('DM_Actuator_Values.xlsx')["FlatProfile"])
with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)    
with open('x0y0.pkl', 'rb') as f: 
    x0y0 = pickle.load(f)    
with open('DM.pkl', 'rb') as f: 
    DM = pickle.load(f)    
    
keys_list = sorted(list(data.keys()))[:-2] # sorts data.dict alphabetically 
keys_list.remove("03_faltprofil")
keys_list.remove("04_0.0V_unwrapped.txt")

x0y0_keys = list(x0y0.keys())
    
    
this_dict = {}

for key in keys_list:
    for position in x0y0_keys:
        a = x0y0[position][0]
        b = x0y0[position][1]
        this_dict[position,str(key)] = data[key][a,b]

        
        
        
        
        
        
        
        
that_keys = list(this_dict.keys())        


i=0
this_list = []
for key in that_keys:
   # for i in range(32):
        if key[0] == 10:
            z= this_dict[key]
            this_list.append(z)
            

plt.plot(this_list)




print("time in seconds: " + str(time.time()-start))



