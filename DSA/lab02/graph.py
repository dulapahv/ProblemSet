pi = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
isPrime0 = [334, 1254, 2644, 4628, 7078, 10027, 13536, 17336, 21808, 26853]
isPrime1 = [7, 13, 20, 30, 39, 50, 65, 76, 87, 100]
isPrime2 = [3, 5, 7, 10, 14, 19, 21, 26, 31, 37]

import matplotlib.pyplot as plt
# plt.plot(pi, isPrime0, label='isPrime0')
plt.plot(pi, isPrime1, label='isPrime1')
plt.plot(pi, isPrime2, label='isPrime2')
plt.legend()
plt.show()
