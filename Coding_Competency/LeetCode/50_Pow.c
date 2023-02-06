#include <stdio.h>

double myPow(double x, int n){
    double factor = x;
    if (n > 0) {
        while (n > 1) {
            x *= factor;
            n--;
        }
    } else {
        while (n <= 0) {
            x /= factor;
            n++;
        }
    }
    return x;
}

int main() {
    printf("%lf", myPow(2.1, 3));
}