import numpy as np
import matplotlib.pyplot as plt


def parabola(t, y):
    """
    t = [0 1 2 3 4 5 6 7 8 9]
    t ** 2 = [0 1 4 9 16 25 36 49 64 81]

    np.vstack([t ** 2, t, np.ones(len(t))]) =
    [[ 0.  1.  4.  9. 16. 25. 36. 49. 64. 81.]
    [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]
    [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]]

    np.vstack([t ** 2, t, np.ones(len(t))]).T = 
    [[ 0.  0.  1.]
    [ 1.  1.  1.]
    [ 4.  2.  1.]
    [ 9.  3.  1.]
    [16.  4.  1.]
    [25.  5.  1.]
    [36.  6.  1.]
    [49.  7.  1.]
    [64.  8.  1.]
    [81.  9.  1.]]

    np.linalg.lstsq(A, y, rcond=None)[0].round(6)
    array([-5.199242 52.199848 16.529091])
    """
    A = np.vstack([t ** 2, t, np.ones(len(t))]).T
    a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
    print(f"y = {c:.6f} {'+' if b >= 0 else ''} {b:.6f} t {'+' if a >= 0 else ''} {a:.6f} t^2")

    plt.plot(t, a * (t ** 2) + (b * t) + c)
    plt.plot(t, y, 'ro')
    plt.show()


t = np.arange(10)
y0 = 20
v0 = 50
dy = np.random.randint(-50, 50, 10)/5
y = y0 + v0*t - 9.8/2 * t**2 + dy
print(t)
print(y)

parabola(t, y)
