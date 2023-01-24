//// lab1_3.cpp
#include <iomanip>
#include <iostream>
#include <vector>

#include "random.hpp"
template <typename T_>
inline constexpr T_ pi_v{3.141592653589793238462643383279502884L};
inline constexpr double pi = pi_v<double>;
int main() {
    constexpr double rnd_min = -1.0, rnd_max = 1.0;
    Rand_double rnd{rnd_min, rnd_max};
    std::random_device rd;
    rnd.seed(rd());
    std::cout << std::fixed << std::setprecision(3);
    double x1 = rnd();
    double y1 = rnd();
    std::cout << "Point #1: (" << x1 << ", " << y1 << ")\n";
    double x2 = rnd();
    double y2 = rnd();
    std::cout << "Point #2: (" << x2 << ", " << y2 << ")";
    std::cout << std::endl;

    constexpr int N = 1000000;
    std::vector<double> x(N), y(N);
    for (int i = 0; i < N; ++i) {
        x[i] = rnd();
        y[i] = rnd();
    }
    int count = 0;
    for (int i = 0; i < N; i++) {
        if (x[i] * x[i] + y[i] * y[i] <= 1.0) {
            count++;
        }
    }
    std::cout << "Estimated PI: " << 4.0 * count / (double)N << std::endl;

    return 0;
}