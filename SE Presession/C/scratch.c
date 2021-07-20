#include <iostream>

using namespace std;

int main() {
    int cases, number;
    scanf("%d", &cases);

    for (int i = 0; i < cases; i++) {
        scanf("%d", &number);
        if (number & 1 == 1) {
            printf("%d is odd\n", number);
        }
        else {
            printf("%d is even\n", number);
        }
    }
}