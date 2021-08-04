#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int days;
    cin >> days;

    int usin[days], temp[days];
    for (int i = 0; i < days; i++) {
        cin >> usin[i];
        temp[i] = usin[i];
    }

    int n = sizeof(temp) / sizeof(temp[0]);
    sort(temp, temp + n);
    
    int least = temp[0];
    for (int i = 0; i < days; i++) {
        if (usin[i] == least) {
            cout << i << endl;
            return 0;
        }
    }
}