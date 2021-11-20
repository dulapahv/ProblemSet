#include <bits/stdc++.h>

using namespace std;

int main() {
    int battery, x ,y;
    int xSum = 0, ySum = 0;
    cin >> battery >> x >> y;
    int list[battery][3];
    for (int i = 0; i < battery; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> list[i][j];
        }
        xSum += list[i][0];
        ySum += list[i][1];
    }
    if (xSum < x || ySum < y) {
        printf("-1");
    }
    else {
        int disX[battery], disY[battery];
        for (int i = 0; i < battery; i++) {
            disX[i] = list[i][0];
            disY[i] = list[i][1];
        }
        sort(disX, disX + battery);
        sort(disY, disY + battery);

        int ans = 0, finAns = 0;
        if (battery == 1 && list[0][0] >= x && list[0][1] >= y) {
            printf("%d", list[0][2]);
            return 0;
        }
        for (int i = 0; i < battery - 1; i++) {
            if (disX[i] + disX[i + 1] >= x && disY[i] + disY[i + 1] >= y) {
                for (int j = 1; j < battery; j++) {
                    if (list[j][0] == disX[i] && list[j][1] == disY[i]) {
                        ans = list[j][2];  
                    }
                }
            }
            finAns += list[ans][2];
        }
        printf("%d", finAns);
    }
}