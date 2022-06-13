#include <stdio.h>


#define size 21
int main() {
    char str[size];
    int i,n_lower,n_upper,n_digits;
    i = n_lower = n_upper = n_digits = 0;
    fgets(str, size,stdin);

    while (str[i] != '\0'){
        if (str[i] >= 'A' && str[i] <= 'Z'){
        n_upper++;
        } else if (str[i] >= 'a' && str[i] <= 'z'){
        n_lower++;
        } else if (str[i] >= '0' && str[i] <= '9'){
        n_digits++;
        }
        i++;
    }
    printf("%d ", n_upper);
    printf("%d ", n_lower);
    printf("%d", n_digits);

}