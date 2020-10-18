from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

x_es = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_es = [4, 5, 1, 2, 3, 7, 6, 4, 9, 8]

xnew = np.arange(1, 10, 0.1)
f_linear = interp1d(x_es, y_es, kind='linear')
f_nearest = interp1d(x_es, y_es, kind='nearest')
f_quadratic = interp1d(x_es, y_es, kind='quadratic')
f_cubic = interp1d(x_es, y_es, kind='cubic')


plt.plot(x_es, y_es, 'o',
         xnew, f_linear(xnew), '-',
         xnew, f_nearest(xnew), '--',
         xnew, f_quadratic(xnew), '.',
         xnew, f_cubic(xnew), '-.')

plt.show()