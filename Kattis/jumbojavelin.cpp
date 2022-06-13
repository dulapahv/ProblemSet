#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int number[cases];
    for (int i = 0; i < cases; i++) {
        cin >> number[i];
    }

    int result = 0;
    for (int i = 0; i < cases; i++) {
        result += number[i];
    }
    result -= (cases - 1);

    cout << result << endl;
}