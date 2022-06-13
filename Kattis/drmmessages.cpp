#include <iostream>

using namespace std;

int main() {
    string usin;
    cin >> usin;

    int x = usin.length() / 2;
    int usin1 = 0, usin2 = 0;
    for (int i = 0; i < x; i++) {
        usin1 += usin[i] - 65;
        usin2 += usin[i + x] - 65;
    }

    while (usin1 > 25) {
        usin1 -= 26;
    }
    while (usin2 > 25) {
        usin2 -= 26;
    }

    for (int i = 0; i < x; i++) {
        usin[i] += usin1;
        if (usin[i] > 'Z') {
            usin[i] = 'A' + (usin[i] - 'Z') - 1;
        }
        usin[i + x] += usin2;
        if (usin[i + x] > 'Z') {
            usin[i + x] = 'A' + (usin[i + x] - 'Z') - 1;
        }
    }
    
    for (int i = 0; i < x; i++) {
        int result = usin[i] + usin[i + x];
        while (result > 25) {
            result -= 26;
        }

        cout << char(result + 65);
    }
}