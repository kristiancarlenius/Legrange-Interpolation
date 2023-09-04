import numpy as np

def f(x):
    return 2**((x**2)-4-x)

def legrange_interpolation(xpoints):
    l = []
    for j in range(len(xpoints)):
        l.append(np.poly1d(xpoints[:j]+xpoints[j+1:], True))
        for i in range(len(xpoints)):
            if(i!=j):
                l[j] *= 1/(xpoints[j]-xpoints[i])
        print(l[j])
    print("-------------------------------")
    ret = 0
    for i in range(len(xpoints)):
        print("f*l:", f(xpoints[i])*l[i])
        ret += f(xpoints[i])*l[i]
    return ret

xpoints = [-1, 0, 1, 2]

print(legrange_interpolation(xpoints))