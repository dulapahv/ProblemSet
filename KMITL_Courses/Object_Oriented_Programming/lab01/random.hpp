//// random.hpp
#ifndef MY_RANDOM_HPP
#define MY_RANDOM_HPP
#include <random>
class Rand_double {
   public:
    using seed_type = std::random_device::result_type;
    Rand_double(double low, double high) : dist{low, high} {}
    // draw an integer number
    double operator()() { return dist(re); }
    // choose new random engine seed
    void seed(seed_type s) { re.seed(s); }

   private:
    std::default_random_engine re;
    std::uniform_real_distribution<double> dist;
};
#endif /* MY_RANDOM_HPP */