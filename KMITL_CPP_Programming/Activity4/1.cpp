#include <iostream>

using namespace std;

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