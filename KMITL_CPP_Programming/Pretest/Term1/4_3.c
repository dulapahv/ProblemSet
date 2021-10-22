#include <stdio.h>

const char text[] = "xyz[20] = { 1, 2, 3 }";

int count_parens(const char *arr, double n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == '=' || arr[i] == ',')
            count++;
    }
    return count;
}

int main() {
    int count = 0;
    double n = sizeof(text)/sizeof(text[0]);
    count_parens(text, n);
    printf("Occurrences: %d\n", count);
    return 0;
}