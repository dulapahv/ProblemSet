#include <stdio.h>

int main() {
    int size, group;
    scanf("%d", &size);
    scanf("%d", &group);

    double num[size];
    for (int i = 0; i < size; i++) {
        scanf("%lf", &num[i]);
    }

    double sum = 0;
    for (int i = 0; i < size - group + 1; i++) {
        sum = 0;
        for (int j = 0; j < group; j++) {
            sum += num[i + j];
        }
        if (i != size - group) {
            printf("%.2lf ", sum / group);
        } else {
            printf("%.2lf", sum / group);
        }
    }
}
