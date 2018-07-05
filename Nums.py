import random as rnd
import nampy as np
from PIL import Image

def get_weights(name):
    w = open('%s.txt'% name, 'r')
    wghts = w.read()
    w.close()
    i=0
    wg = []
    for line in wghts.split('\n'):
        wg.append([])
        for s in line.split(' '):
            wg[i].append(float(s))
        i+=1
    return wg
def activate(C):
    if(C>=0.5):
        return 1
    else:
        return 0
def GetNum(pix):
    Hidden_Layer_weights=get_weights('Weights')
    Hidden_Layer=np.multiply(pix,Hidden_Layer_weights)
    Hidden_Layer_Output=[[]]
    for el in Hidden_Layer[0]:
        Hidden_Layer_Output[0].append(activate(el))
    Output_Layer_weights=get_weights('WeightsOut')
    Output_Layer=np.multiply(Hidden_Layer_Output,Output_Layer_weights)
    Output=[[]]
    for el in Output_Layer[0]:
        Output[0].append(activate(el))
    return Output[0][0]
def Start(i):
    image = Image.open("temp%i.jpg"%i) 
    w = image.size[0]  
    h = image.size[1] 	
    pix = image.load()
    pixels=[[]]
    for i in range(w):
        for j in range(h):
            pixels[0].append(abs(round(1-int(pix[i,j][0])/255,1)))
    if GetNum(pixels)!=1:
        Learn(pixels,'Weights')
def Learn(pixels,wg):
    weights=get_weights(wg)
    for line in range (len(weights)):
        for el in range (len(weights[0])):
            if pixels[0][el]>0:
                weights[line][el]=round(rnd.uniform(-1,1),2)
    w=open('%s.txt'%wg,'w')
    for line in range (len(weights)):
        if(line!=0):
            w.write('\n')
        for el in range (len(weights[0])):
            if(el!=0):
                w.write(' ')
            w.write(str(weights[line][el]))
    w.close()
