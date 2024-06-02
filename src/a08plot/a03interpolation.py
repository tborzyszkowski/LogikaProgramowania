import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

n = 10
x = np.linspace(0, 4, n)
y = np.cos(x**2/3+4)+ 0.1 * np.random.randn(n)
print(x)
print(y)
f1 = interp1d(x, y, kind = 'linear')
f2 = interp1d(x, y, kind = 'quadratic')

xnew = np.linspace(0, 4, 100)
print(xnew)

f, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(x, y, 'o', xnew, f1(xnew), '-')
ax[1].plot(x, y, 'o', xnew, f2(xnew), '-')
plt.show()