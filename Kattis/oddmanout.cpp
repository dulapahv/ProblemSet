#include <iostream>
#include <vector>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    int ppl[cases];
    vector<int> usin;
    for (int i = 0; i < cases; i++) {
        cin >> ppl[cases];

        for (int j = 0; j < ppl; j++) {
            int temp;
            cin >> temp;
            usin.push_back(temp);
        }
    }

    for (int i = 0; i < cases; i++) {
        for (int j = 0; j < ppl; j++) {
            for (int k = 0; k < ppl; k++) {
                if (usin[j] )
            }
        }
    }
}