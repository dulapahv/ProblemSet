#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int people;
    vector<int> usin;
    for (int i = 0; i < cases; i++) {
        cin >> people;

        int temp;
        for (int j = 0; j < cases; j++) {
            cin >> temp;
            usin.push_back(temp);
        }
    }

    cout << usin[1] << endl;
}