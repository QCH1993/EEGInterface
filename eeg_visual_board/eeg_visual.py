import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def Visualeeg_sensor2D(name,loc):
    X = loc[:,0]
    Y = loc[:,1]
    plt.figure("sensor_2D")
    for i in range(len(name)):
        plt.scatter(X[i],Y[i],marker='o')
        plt.text(X[i],Y[i],name[i])
    plt.legend()
    plt.show()

def Visualeeg_sensor3D(name,loc):
    X = loc[:,0]
    Y = loc[:,1]
    Z = loc[:,2]
    plt.figure("sensor_3D")
    ax = plt.subplot(111,projection='3d')

    for i in range(len(name)):
        ax.scatter(X[i],Y[i],Z[i],c='r')
        ax.text(X[i],Y[i],Z[i],name[i])
    plt.legend()
    plt.show()


def Visualeeg32_subplot(eegdata,name):
    plt.figure(name+'_32subplot')
    channels,points = eegdata.shape
    width = 8
    i = 1

    for eegdata_single_channel in eegdata[0:32,0::]:
        print(i)
        print(width)
        plt_ = plt.subplot(width,4,i)
        plt_.plot(range(points),eegdata_single_channel,label=str(i))

        i=i+1
        plt_.legend()
    plt.show()

def Visualeeg32_one(eegdata,name):
    plt.figure(name+'_32one')
    channels,points = eegdata.shape
    i = 1
    print("one:",eegdata.shape)
    for eegdata_single_channel in eegdata[0:32,0::]:
        color = (i*7,i*7,i*7)
        plt.plot(range(points),eegdata_single_channel,label=str(i))

        i=i+1
    plt.legend()
    plt.show()
