#include <iostream>

using namespace std;

int main() {
    int ppl, chicken;
    cin >> ppl >> chicken;

    if (ppl < chicken) {
        int diff = chicken - ppl;
        if (diff > 1) {
            cout << "Dr. Chaz will have " << diff << " pieces of chicken left over!" << endl;
        }
        else {
            cout << "Dr. Chaz will have " << diff << " piece of chicken left over!" << endl;
        }
    }
    else {
        int diff = ppl - chicken;
        if (diff > 1) {
            cout << "Dr. Chaz needs " << diff << " more pieces of chicken!" << endl;
        }
        else {
            cout << "Dr. Chaz needs " << diff << " more piece of chicken!" << endl;
        }
    }
}