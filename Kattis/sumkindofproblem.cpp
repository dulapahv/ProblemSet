#include <iostream>

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

    int s1[cases] = {0}, s2[cases] = {0}, s3[cases] = {0};
    for (int i = 0; i < cases; i++) {
        for (int j = 0; j <= usin[i][1]; j++) {
            s1[i] += j;
        }

        int counts2 = 0, x = 0;
        while (counts2 < usin[i][1]) {
            if (x & 1) {
                s2[i] += x;
                counts2++;
            }
            x++;
        }

        int counts3 = 0, y = 0;
        while (counts3 <= usin[i][1]) {
            if (y % 2 == 0) {
                s3[i] += y;
                counts3++;
            }
            y++;
        }
    }

    for (int i = 0; i < cases; i++) {
        cout << usin[i][0] << " " << s1[i] << " " << s2[i] << " " << s3[i] << endl;
    }
    
}