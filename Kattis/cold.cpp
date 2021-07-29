#include <iostream>

using namespace std;

int main() {
    int days;
    cin >> days;

    int temp[days];
    for (int i = 0; i < days; i++) {
        cin >> temp[i];
    }

    int count = 0;
    for (int i = 0; i < days; i++) {
        if (temp[i] < 0) {
            count += 1;
        }
    }

    cout << count << endl;
}