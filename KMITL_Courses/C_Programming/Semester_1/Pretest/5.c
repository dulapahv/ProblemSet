#include <stdio.h>

int main()
{
    double arr[] = {8, 6.2, 3.1, 4};
    float sum = 0, count;

    count = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < count; i++)
        printf("%f ", arr[i] * arr[i]);
    return 0;
}