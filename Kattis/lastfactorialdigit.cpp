#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int number[cases];
    for (int i = 0; i < cases; i++) {
        cin >> number[i];
    }

    int result[cases];
    for (int i = 0; i < cases; i++) {
        int fact = 1;
        for (int j = 1; j <= number[i]; j++) {
            fact *= j;
            result[i] = fact % 10;
        }
    }

    for (int i = 0; i < cases; i++) {
        cout << result[i] << endl;
    }
}