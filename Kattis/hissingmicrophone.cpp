#include <iostream>

using namespace std;

int main() {
    string str;
    cin >> str;

    for (int i = 1; i < str.length(); i++) {
        if (str[i-1] == 's' && str[i] == 's') {
            cout << "hiss" << endl;
            exit(0);
        }
    }
    cout << "no hiss" << endl;
}