#include <stdio.h>

int main() {
    float x, y;
    int i;
    scanf("%f%f%d", &x, &y, &i);

    if (i <= 0 || i >= 5) {
        printf("Invalid operation");
        return 0;
    }
        
    switch (i) {
        case 1:
            printf("%2.f", x + y);
            break;
        
        case 2:
            printf("%.2f", x - y);
            break;

        case 3:
            printf("%.2f", x * y);
            break;
        
        case 4:
            printf("%.2f", x / y);
            break;
    }
}
