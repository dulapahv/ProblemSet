#include <stdio.h>

double compute(double num) {
    return ((8 * (num * num)) + (2 * num) + 5);
}

int main() {
    printf("%lf", compute(5));
    return 0;
}