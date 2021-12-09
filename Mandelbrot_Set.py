import matplotlib.pyplot as plt
import numpy as np

xx = np.arange(-2.000, 1.005, 0.005)
yy = np.arange(-2.000, 2.005, 0.005)

cc = [complex(x,y) for x in xx for y in yy]

result = []

for c in cc:
    z_n = 0
    z_nplus1 = 0
    colour = 0
    for n in range(50):
        z_nplus1 = z_n**2 + c
        z_n = z_nplus1
        if(abs(z_nplus1) > 20):
            colour = n
            result.append([c, colour])
            break
        if n == 49:
            result.append([c, 49])    


x = [a[0].real for a in result]
y = [b[0].imag for b in result]
colour = [c[1] for c in result]

plt.scatter(x, y, c = colour, s=1, cmap = "binary")
plt.show()
