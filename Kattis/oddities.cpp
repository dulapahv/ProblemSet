#include <iostream>

using namespace std;

int main() {
    int cases, number[20];
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        scanf("%d", &number[i]);
    }

    for (int i = 0; i < cases; i++) {
        if (number[i] & 1 == 1) {
            printf("%d is odd\n", number[i]);
        }
        else {
            printf("%d is even\n", number[i]);
        }
    }
}