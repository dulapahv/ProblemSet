#include <iostream>

typedef unsigned long long ull;

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int stud;
    for (int i = 0; i < cases; i++) {
        cin >> stud;

        ull candy[stud], sum = 0;
        for (int j = 0; j < stud; j++) {
            cin >> candy[j];
            sum += candy[j] % stud;
        }

        if (sum % stud == 0) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}