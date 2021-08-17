#include <iostream>

using namespace std;

int main() {
    int height;
    cin >> height;

    for (int i = 0; height < height; i++) {
        for (int j = 0; j < height - i; j++) {
            cout << "*";
        }
        cout << endl;
    }
}