from matplotlib import pyplot as plt
from scipy.interpolate import interp1d


def wykres_podstawowy(dane):
    y_es = [k["kurs_max"] for k in dane]
    x_es = range(0, len(y_es))
    f_linear = interp1d(x_es, y_es, kind='linear')
    # xnew = np.arange(1, len(y_es), 0.1)

    plt.plot(x_es, y_es, 'o',
             x_es, f_linear(x_es), '-')
    plt.show()