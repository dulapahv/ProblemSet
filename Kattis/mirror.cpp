#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int a, b;
    for (int i = 0; i < cases; i++) {
        cin >> a >> b;

        char usin[a][b];
        for (int j = 0; j < a; j++) {
            for (int k = 0; k < b; k++) {
                cin >> usin[j][k];
            }
        }

        cout << "Test " << i + 1 << endl;
        
        for (int j = a - 1; j >= 0; j--) {
            for (int k = b - 1; k >= 0; k--) {
                cout << usin[j][k];
            }
            cout << endl;
        }
    }
}