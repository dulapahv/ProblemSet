#include <iostream>

using namespace std;

int main() {
    string usin;
    string str = "FBI";
    for (int i = 0; i < 5; i++) {
        cin >> usin;

        if (usin.find(str) == 0) {
            cout << i << endl;
        }
        else {
            cout << "HE GOT AWAY!" << endl;
        }
    }
}