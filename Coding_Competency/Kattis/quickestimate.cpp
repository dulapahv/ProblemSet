#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    string usin;
    int result[cases];
    for (int i = 0; i < cases; i++) {
        cin >> usin;
        result[i] = usin.length(); 
    }

    for (int i = 0; i < cases; i++) {
        cout << result[i] << endl;
    }
}