#include <iostream>

using namespace std;

int main() {
    int all, voted;
    cin >> all >> voted;

    int votedScore = 0, temp;
    for (int i = 0; i < voted; i++) {
        cin >> temp;
        votedScore += temp;
    }

    float high = votedScore, low = votedScore;
    for (int i = voted; i < all; i++) {
        low += -3;
        high += 3;
    }

    cout << low / all << " " << high / all << endl;
}