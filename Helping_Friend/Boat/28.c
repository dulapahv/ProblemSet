#include <stdio.h>

#define N 10
int DATA[N] = {1,6,-7,0,14,55,95,-41,7,33};
int value;
int n_gt;

int count_gt(int v) {

    int n_gt;
    
    for (int i = 0; i < N; i++)
        if (DATA[i] > v)
            n_gt++;
    
    return n_gt;

}

int main() {
    
    
    scanf("%d", &value);
    printf("%d\n", count_gt(value));
    
    return 0;
}