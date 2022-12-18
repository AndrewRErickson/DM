from sklearn import metrics
import numpy as np
import time
import pickle
from lmfit import Model
import pandas as pd
import matplotlib.pyplot as plt
start = time.time()

### Import Data 

with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)    
with open('x0y0.pkl', 'rb') as f: 
    x0y0 = pickle.load(f)    
with open('DM.pkl', 'rb') as f: 
    DM = pickle.load(f)    
    
keys_list = sorted(list(data.keys())) # sorts data.dict alphabetically 

x0y0_keys = list(x0y0.keys())
    
    
actuator_map = {}
for key in keys_list:
    v = np.asarray(pd.read_excel('DM_Actuator_Values.xlsx')["FlatProfile"])
    
    v[key[0]]=key[1]
    
    actuator_map[key]=((v,data[key]))


with open('actuator_map.pkl', 'wb') as f:
    pickle.dump(actuator_map, f)

print("time in seconds: " + str(time.time()-start))



