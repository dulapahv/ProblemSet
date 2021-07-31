#include <iostream>
#include <string>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        string a, b;
        cin >> a >> b;

        cout << a << endl;
        cout << b << endl;

        int size = a.size();
        for (int j = 0; j < size; j++) {
            if (a[j] == b[j]) {
                cout << '.';
            }
            else {
                cout << '*';
            }
        }

        cout << endl << endl;
    }
}