#include <iostream>

using namespace std;

// Driver Code
int main() {
    int height;
    cout << "Height: ";
    cin >> height;
 
    for (int i = height; i > 0; i--) {
        for (int j = 0; j < height - i; j++)
            cout << " ";
        for (int j = 0; j < i; j++) {
            cout << "*";
        }
        cout << endl;
    }
}