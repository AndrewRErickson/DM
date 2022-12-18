from sklearn import metrics
import numpy as np
import time
import pickle
from lmfit import Model
import pandas as pd
import matplotlib.pyplot as plt
start = time.time()

### Import Data 
voltages = pd.read_excel('DM_Actuator_Values.xlsx')
with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)    
with open('x0y0.pkl', 'rb') as f: 
    x0y0 = pickle.load(f)    
    
    
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

### Regression function
def regress(actu):
    x0 = x0y0[actu][0]
    y0 = x0y0[actu][1]
    v=1.0
    mx=x0+10
    nx=x0-10
    my=y0+10
    ny=y0-10
    
    relative_x0 = x0-nx
    relative_y0=y0-ny
    
    print('x0', x0,'y0',y0,'mx',mx,'nx',nx,'my',my,'ny',ny)
    x = []
    y = []
    for i in np.arange(nx,mx,1):
        for j in np.arange(ny,my,1):
            x.append(i)
            y.append(j)
    x=np.asarray(x)
    y=np.asarray(y)

    xx, yy = np.meshgrid(np.arange(mx,nx,-1), np.arange(my,ny,-1))

    def z(x,y,v,a,x0,y0,sx,sy,offset):    
        return a*v*np.exp(-(((x-x0)**2)/(sx**2))-(((y-y0)**2)/(sy**2)))+offset
    z0 = data[(actu,v)][nx:mx,ny:my]
    z0_shape = np.shape(z0)
    z1 =  z0.flatten()
    gmodel = Model(z, independent_vars=['x','y'],nan_policy='omit')
    gmodel.set_param_hint('v',vary=False)
    gmodel.set_param_hint('a',min = 0, max = 3000)
    gmodel.set_param_hint('x0', vary =False)
    gmodel.set_param_hint('y0', vary = False)
    gmodel.set_param_hint('sx',min = 0, max = 70)
    gmodel.set_param_hint('sy',min = 0, max = 70)
    results = gmodel.fit(z1, y=y, x=x,v=v,a=1000, x0=x0, y0=y0, sx=20,sy=20, 
                         offset = 1500)
    p = results.params.valuesdict()
    z_fit = z(x,y,v,p["a"],p['x0'],p['y0'],p['sx'],p['sy'],p['offset'])

    z2 = (np.reshape(z_fit,z0_shape))
    ax.plot_wireframe(xx,yy,z0,rstride=20, cstride=20, 
                      label ='data', color = 'black')

    ax.plot_wireframe(xx, yy, z2, rstride=20, cstride=20,label = 'model',
                      color = 'red')
    
    ax.set_xlim(0,450)
    ax.set_ylim(0,450)
    ax.set_zlim(0,3000)
    ax.scatter(x0,y0,z0[relative_x0,relative_y0], color = 'green')
    
    
    model_max = (np.asarray(np.unravel_index(z2.argmax(), z2.shape)))
    
    model_x0=model_max[0]
    model_y0=model_max[1]
    relative_model_x0 =model_x0+nx 
    relative_model_y0 = model_y0+ny
    
    ax.scatter(relative_model_x0,relative_model_y0, z2[model_x0,model_y0],color = 'blue')
    ax.set_title('actuator'+str(actu))
    ax.legend()
    print("mean squared error: ", metrics.mean_squared_error(z0,z2))
    print("R^2: ", metrics.r2_score(z0,z2))



#regress(2)
### User input for actuator 

#actuators = list(map(int, input('Enter actuators separated with a space: ').split()))
actuators = np.arange(32)
for item in actuators:
    regress(int(item))



