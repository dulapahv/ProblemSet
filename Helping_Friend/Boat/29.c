#include <stdio.h>

#define N 10
int DATA[N];

int find_index(int v) {

    int found_index;

    for (int i = 0; i < N; i++)
        if (DATA[i] == v)
            return i;
    found_index = -1;

    return found_index;
}

int main() {
    int target, found_index;

    for (int i = 0; i < N; i++)
        scanf("%d", &DATA[i]);
    scanf("%d", &target);
    found_index = find_index(target);
    found_index != -1 ? printf("Found at %d", found_index) : printf("Not found");

    return 0;
}