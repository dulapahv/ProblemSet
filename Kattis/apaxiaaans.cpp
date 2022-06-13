#include <iostream>
#include <string>

using namespace std;

int main() {
    string usin, output;
    cin >> usin;

    int x = 1;
    while (usin[x] != NULL)
    {
        if (usin[x-1] != usin[x]) {
            output[x] += usin[x];
        }
        x += 1;
    }
    
    cout << output << endl;
}