#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int phone;
    for (int i = 0; i < cases; i++) {
        
        cin >> phone;

        int usin;
        int storage[phone];
        for (int j = 0; j < phone; j++) {
            while (cin >> usin) {
                storage[j] == usin;
            }
        }

        for (int j = 1; j < phone; j++) {
            for (int k = 0; k < sizeof(storage[j]); k++) {
                if (storage[0] == storage[j]) {
                    cout << "NO" << endl;
                }
                else {
                    cout << "YES" << endl;
                }
            }
        }
    }
}
