#include <stdio.h>

int MIN_VAL = -4;
int MAX_VAL = 42;

void clip_value(int arrSize, int *arr) {
    for (int i = 0; i < arrSize; i++) {
        if (arr[i] < MIN_VAL)
            arr[i] = MIN_VAL;
        else if (arr[i] > MAX_VAL)
            arr[i] = MAX_VAL;
    }
}

int main() {
    int arrSize;
    scanf("%d", &arrSize);

    int arr[arrSize];
    for (int i = 0; i < arrSize; i++)
        scanf("%d", &arr[i]);

    clip_value(arrSize, arr);
    for (int i = 0; i < arrSize; i++)
        printf("%d ", arr[i]);
}