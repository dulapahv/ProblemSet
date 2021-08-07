#include <iostream>

using namespace std;

int main() {
    string msg;
    cin >> msg;

    string key;
    for (int i = 0; i < msg.length(); i++) {
        key[0] = 'A';
        key[1] = 'C';
        key[2] = 'M';
        key[i + 3] = msg[i];
    }

    // for (int i = 0; i < msg.length(); i++) {
    //     cout << ciph[i];
    // }
}