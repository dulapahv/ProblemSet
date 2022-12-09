#include <stdio.h>

int test_range(int i)
{
    if (i <= 0)
        return 1;
    else if (i >= 10)
        return 1;
    else
        return 0;
}

int main() {
    printf("%d\n", test_range(0));
    printf("%d\n", test_range(10));
    printf("%d\n", test_range(5));
}