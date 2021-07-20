#include <stdio.h>

void swapDouble(double *xPtr, double *yPtr) {
    double temp = *xPtr;
    *xPtr = *yPtr;
    *yPtr = temp;
}

int main() {
    double x, y;
    printf("x = ");
    scanf("%lf", &x);
    printf("y = ");
    scanf("%lf", &y);
    swapDouble(&x, &y);
    printf("x = %lf y = %lf", x, y);
    return 0;
}