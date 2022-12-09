#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int score[cases];
    for (int i = 0; i < cases; i++) {
        cin >> score[i];
    }

    float result, count = 0;
    for (int i = 0; i < cases; i++) {
        if (score[i] >= 0) {
            count += 1;
            result += score[i];
        }
    }
    result /= count;

    cout << result << endl;
}