# this program gets all of the uncropped xyz data. That means don't use this for just a quick run

import numpy as np
import os
import time
import pickle
startTime = time.time()

z_dict = {}

startactuator = 0
stopactuator = 32

# =============================================================================
# for n in np.arange(startactuator, stopactuator, 1):
#     if n < 10:
#         n = '0'+str(n)
#     else:
#         n = str(n)
#     folder_path = '/Users/andrewerickson/Documents/Research/DeformableMirrorConfigurations/12.30.2019/Actuator' + \
#         n+'/PhaseMaps_Unwrapped'
#     files = os.listdir(folder_path)
#     for filename in files:
#         if '.DS_Store' not in filename:
#             file = np.loadtxt(os.path.join(folder_path, filename))
#             z = file*633/(4*np.pi)
#             z = z-np.amin(z)
#             key =str(n) + '_' + str(filename).strip('V_unwrapped')
#             z_dict[key]=z
# =============================================================================
for n in np.arange(startactuator, stopactuator, 1):
    if n < 10:
        k = '0'+str(n)
    else:
        k = str(n)
    folder_path = '/Users/andrewerickson/Documents/Research/DeformableMirrorConfigurations/12.30.2019/Actuator' + \
        k+'/PhaseMaps_Unwrapped'
    files = os.listdir(folder_path)
    for filename in files:
        if '.DS_Store' not in filename:
            file = np.loadtxt(os.path.join(folder_path, filename))
            z = file*633/(4*np.pi)
            z = z-np.amin(z)
            if "faltprofil" in filename:
                print('no')
            elif "0.0V_unwrapped.txt" in filename:
                None
            else:
                key =(n,float(str(filename).strip('V_unwrapped.txt')))
                z_dict[key]=z

with open('uncropped_z.pkl', 'wb') as f:
    pickle.dump(z_dict, f)
    

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
print('Execution time in minutes: ' + str(executionTime/60))