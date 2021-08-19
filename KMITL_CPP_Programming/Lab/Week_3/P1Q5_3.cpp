#include <iostream>
#include <string>

using namespace std;

void to_lower(string str) {
    for (int i = 0; i < str.length(); i++) {
        cout << char(toupper(str[i]));
    }
}

int main() {
    string usin;
    getline(cin, usin);
    to_lower(usin);
}