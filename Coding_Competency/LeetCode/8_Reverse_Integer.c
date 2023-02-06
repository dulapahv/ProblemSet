#include <limits.h>
#include <stdio.h>

int reverse(int x) {
    int ans = 0;
    int sign = x < 0 ? -1 : 1;
    x = (int)(unsigned)x;

    while (x > 0) {
        int rem = x % 10;
        if (ans > INT_MAX / 10 || (ans == INT_MAX / 10 && rem > 7)) {
            return 0;
        }
        if (ans < INT_MIN / 10 || (ans == INT_MIN / 10 && rem < -8)) {
            return 0;
        }
        ans = ans * 10 + rem;
        x /= 10;
    }
    return sign * ans;
}

int main() {
    printf("\n%d", reverse(-123));
}