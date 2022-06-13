#include <iostream>

using namespace std;

int main() {
    int questions;
    cin >> questions;

    char usin[questions];
    for (int i = 0; i < questions; i++) {
        cin >> usin[i];
    }

    int result = 0;
    for (int i = 1; i < questions; i++) {
        if (usin[i-1] == usin[i]) {
            result += 1;
        }
    }

    cout << result << endl;
}