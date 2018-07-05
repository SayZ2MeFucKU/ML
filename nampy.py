def multiply (a1,a2):
    if len(a1[0])!=len(a2[0]):
        print("Length Error!")
        return None
    else:
        a3=[]
        for i in range(len(a1)):
            a3.append([])
        for i in range(len(a1)):
            for j in range(len(a2)):
                s=0.0
                for k in range(len(a1[0])):
                    s+=a1[i][k]*a2[j][k]
                a3[i].append(s)
        return a3
