#include <stdio.h>
#include <string.h>

int main() {
    char str[5];

    memset(str, '$', sizeof(str));
    str[sizeof(str)] = '\0';
    puts(str);

    int arr[10];
    memset(arr, 0, sizeof(arr));
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }

    return (0);
}