#include <stdio.h>

int main() {
    int c, zero = 0, one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0;
    printf("Enter a text: ");
    while (c != '\n') {
        scanf("%c", &c);
        switch (c) {
            case '0':
                zero++;
                break;
            case '1':
                one++;
                break;
            case '2':
                two++;
                break;
            case '3':
                three++;
                break;
            case '4':
                four++;
                break;
            case '5':
                five++;
                break;
            case '6':
                six++;
                break;
            case '7':
                seven++;
                break;
            case '8':
                eight++;
                break;
            case '9':
                nine++;
                break;
        }
    }
    printf("Digit:       0 1 2 3 4 5 6 7 8 9\n");
    printf("Occurrences: %d %d %d %d %d %d %d %d %d %d\n", zero, one, two, three, four, five, six, seven, eight, nine);
}