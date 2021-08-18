#include <iostream>
#include <string>

using namespace std;

void to_lower(string *strPtr) {
    string temp = *strPtr;
    *strPtr = ;
}

int main() {
    string usin;
    getline(cin, usin);

    to_lower(&usin);
    cout << usin << endl;
}