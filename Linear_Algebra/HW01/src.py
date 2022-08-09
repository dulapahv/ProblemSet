import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


def color_mix(c1, c2):
    return (np.array(c1) * 0.5) + (np.array(c2) * 0.5)


red = mcolors.to_rgb([1, 0, 0])
green = mcolors.to_rgb([0, 1, 0])
blue = mcolors.to_rgb([0, 0, 1])
mycolor = color_mix(red, green)
plt.plot(2, 4, 'o', color=mycolor, markersize=50)

# plt.show()
