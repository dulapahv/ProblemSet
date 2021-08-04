#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int usin[cases][2];
    for (int i = 0; i < cases; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> usin[i][j];
        }
    }

    vector<int> temp;
    for (int i = 0; i < cases; i++) {
        for (int j = usin[i][0]; j <= usin[i][1]; j++) {
            temp.push_back(j);
        }
    }

    int date[temp.size()];
    copy(temp.begin(), temp.end(), date);

    int n = sizeof(date) / sizeof(date[0]);
    sort(date, date + n);

    vector<int> result;
    for (int i = 0; i < temp.size(); i++) {
        if (date[i] != date[i + 1]) {
            result.push_back(date[i]);
        }
    }

    cout << result.size() << endl;
}