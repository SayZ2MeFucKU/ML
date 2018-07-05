w=open('WeightsOut.txt','w')
for i in range(10):
    if (i!=0):
        w.write('\n')
    for j in range(16):
        if (j!=0):
            w.write(' ')
        w.write('0')
w.close()
w=open('Weights.txt','w')
for i in range(16):
    if (i!=0):
        w.write('\n')
    for j in range(784):
        if (j!=0):
            w.write(' ')
        w.write('0')
w.close()
print('Write Success')
