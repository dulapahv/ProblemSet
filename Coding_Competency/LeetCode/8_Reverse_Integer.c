#include <stdio.h>
#include <limits.h>

int reverse(int x) {
    if (x > INT_MAX || x < INT_MIN) {
        return 0;
    }
    int ans = 0;
    int i = 1;
    int len = 0;
    int sign = 1;
    if (x < 0) {
        sign = -1;
        x *= -1;
    }
    int temp = x;
    while (temp > 0) {
        temp /= 10;
        i *= 10;
        len++;
    }
    i /= 10;
    while (len > 0) {
        ans += (x % 10) * i;
        x /= 10;
        i /= 10;
        len--;
    }
    return sign * ans;
}

int main() {
    printf("\n%d", reverse(153423646));
}