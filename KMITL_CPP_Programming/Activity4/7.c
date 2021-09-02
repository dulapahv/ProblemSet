// #include <stdio.h>

// #define SIZE 10

// void find_two_largest(const int* a, int n, int* largest, int* second_largest);

// int main() {
//     int a[SIZE] = {38, 4, 38, 84, 65, 9, 5, 14, 76, 49};
//     int largest = 0, second_largest = 0;

//     printf("Elements in array are: ");
//     for (int i = 0; i < SIZE; i++)
//         printf("%d ", a[i]);

//     find_two_largest(a, SIZE, &largest, &second_largest);
//     printf("\nLargest: %d\nSecond Largest: %d\n", largest, second_largest);
// }

void find_two_largest(const int* a, int n, int* largest, int* second_largest) {
    for (int i = 0; i < n; i++) {
        if (a[i] > *largest) {
            *second_largest = *largest;
            *largest = a[i];
        }
        else if (a[i] <= *largest && a[i] > *second_largest)
            *second_largest = a[i];
    } 
}