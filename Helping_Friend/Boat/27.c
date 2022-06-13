#include <stdio.h>

int find_min(int min, int input); // function prototype

int main() {
    int num[2], ans;

    for (int i = 0; i < 2; i++)
        scanf("%d", &num[i]);
    
    ans = num[0];

    for (int i = 0; i < 2; i++)
        ans = find_min(ans, num[i]);
    
    printf("%d\n", ans);
}

int find_min(int min, int input) {
    if (input < min) {
        return input;
    }
    return min;
}