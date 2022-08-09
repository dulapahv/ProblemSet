# import numpy as np

# e = [1, 2, 3]
# f = [4, 5, 6]

# v1 = np.array(e)
# v2 = np.array(f)

# print(v1 + v2)

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
red = mcolors.to_rgb([1, 0, 0])
green = mcolors.to_rgb([0, 1, 0])
blue = mcolors.to_rgb([0, 0, 1])

plt.plot(2, 4, 'o')
plt.plot(2, 4, 's')
plt.plot(2, 4, 'ro')
plt.plot(2, 4, 'o', color='r', markersize=50)
plt.plot(2, 4, 'o', color=green, markersize=50)

plt.show()
