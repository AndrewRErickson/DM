from sklearn import metrics
import numpy as np
import time
import pickle
from lmfit import Model
import pandas as pd
import matplotlib.pyplot as plt
start = time.time()

############# #import data ##############
voltages = pd.read_excel('DM_Actuator_Values.xlsx')

with open('uncropped_z.pkl', 'rb') as f: 
    data = pickle.load(f)    
with open('x0y0.pkl', 'rb') as f: 
    x0y0 = pickle.load(f)    

def regress(actu):

    x0 = x0y0[actu][0]
    y0 = x0y0[actu][1]

    v=1.0

    mx=484
    nx=0

    my=484
    ny=0

    x = []
    y = []

    for i in np.arange(mx,nx,-1):
        for j in np.arange(ny,my,1):
            x.append(i)
            y.append(j)
        
    x=np.asarray(x)
    y=np.asarray(y)

    xx, yy = np.meshgrid(np.arange(nx,mx,1), np.arange(nx,mx,1))

    def z(x,y,v,a,x0,y0,sx,sy,offset):    
        return a*v*np.exp(-(((x-x0)**2)/(sx**2))-(((y-y0)**2)/(sy**2)))+offset
    
    if actu < 10:
        z0 = data["0"+str(actu) + '_' +str(v)][nx:mx,ny:my]
    else:
        z0 = data[str(actu) + '_' +str(v)][nx:mx,ny:my]
        
    z0_shape = np.shape(z0)
    z1 =  z0.flatten()

    gmodel = Model(z, independent_vars=['x','y'],nan_policy='omit')
    gmodel.set_param_hint('v',vary=False)
    gmodel.set_param_hint('a',min = 0, max = 3000)
    gmodel.set_param_hint('x0', vary =False)
    gmodel.set_param_hint('y0', vary = False)
    gmodel.set_param_hint('sx',min = 0, max = 70)
    gmodel.set_param_hint('sy',min = 0, max = 70)
    results = gmodel.fit(z1, y=y, x=x,v=v,a=1000, x0=x0, y0=y0, sx=20,sy=20, offset = 1500)
    p = results.params.valuesdict()

    z_fit = z(x,y,v,p["a"],p['x0'],p['y0'],p['sx'],p['sy'],p['offset'])
    print(np.shape(z_fit))

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    z2 = (np.reshape(z_fit,z0_shape))
    
    
    
    
#    ax.plot_wireframe(xx,yy,z0[nx:mx,ny:my],rstride=20, cstride=20, label ='data', color = 'black')
    ax.set_xlim(0,500)
    ax.set_ylim(0,500)
    ax.set_zlim(0,3000)

    ax.plot_wireframe(xx, yy, z2, rstride=20, cstride=20,label = 'model',color = 'red')
    ax.scatter(y0,x0,z0[x0,y0], color = 'green')
    #ax.text(x0,y0,z0[x0,y0], str(x0)+","+str(y0))

    model_max = np.asarray(np.unravel_index(z2.argmax(), z2.shape))
    print(model_max)
    ax.scatter(model_max[0],model_max[1], color = 'blue')
    #ax.text(model_max[0],model_max[1],z2[model_max], str(x0)+","+str(y0))

    ax.set_title('actuator'+str(actu))
    ax.legend()



    print(metrics.mean_squared_error(z0[nx:mx,ny:my],z2))
    print(metrics.r2_score(z0[nx:mx,ny:my],z2))
    
    

regress(0)



