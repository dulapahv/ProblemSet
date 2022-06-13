#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int usin[cases];
    for (int i = 0; i < cases; i++) {
        cin >> usin[i];
    }

    int n = sizeof(usin)/sizeof(usin[0]);
    sort(usin, usin + n);

    vector<int> result;
    for (int i = 0; i < cases - 1; i++) {
        if (usin[i] != i + 1) {
            result.push_back(i + 1);
        }
    }

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }
}