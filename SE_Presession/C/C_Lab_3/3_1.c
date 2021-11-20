#include <stdio.h>

#define SIZE 5

void swap(int *xPtr, int *yPtr) {
    int temp = *xPtr;
    *xPtr = *yPtr;
    *yPtr = temp;
}

int main() {
    int arr[SIZE];

    for (int i = 0; i < SIZE; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < SIZE-1; i++) {
        for (int j = 0; j < SIZE-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(&arr[j], &arr[j+1]);
            }       
        }
    }

    for (int i = 0; i < SIZE; i++) {
        printf("%d ", arr[i]);
    }
}