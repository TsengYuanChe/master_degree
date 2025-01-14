import numpy as np

const = -13.513005539374699282006986322812736034393310546875

def formula1(x):
    y = -2.99368*np.log10(x) - 1.53106
    return y

def formula2(x):  #18526
    y = -3.00595*np.log10(x) - 0.68428
    return y

def formula3(x): #26225
    y = -3.01430*np.log10(x) - 0.19365
    return y

def formula4(x): #32962
    y = -3.02535*np.log10(x) + 0.15558
    return y

#print(formula4(32960))

for i in range(9990, 10010):
    diff = formula1(i) - const
    print(abs(diff), i)