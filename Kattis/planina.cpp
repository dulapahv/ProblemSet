#include <iostream>

using namespace std;

int main() {
    int usin;
    cin >> usin;

    int result = 3;
    for (int i = 1; i < usin; i++) {
        result = (result * 2) - 1;
    }

    cout << result * result << endl;
}