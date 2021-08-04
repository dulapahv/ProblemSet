#include <iostream>

#define SIZE 5

using namespace std;

void swap(int *xPtr, int *yPtr) {
    int temp = *xPtr;
    *xPtr = *yPtr;
    *yPtr = temp;
}

int main() {
    int arr[SIZE];

    for (int i = 0; i < SIZE; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                
                for (int k = 0; k < SIZE; k++) {
                cout << arr[k] << " ";
                }
                
                cout << endl;
            }
        }
    }
}