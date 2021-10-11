#include <stdio.h>

int main() {
    int n, m;
    scanf("%d ", &n);
    scanf("%d ", &m);
    
    int matrix1[n][m], matrix2[n][m], matrixAns[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &matrix1[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", &matrix2[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            matrixAns[i][j] = matrix1[i][j] + matrix2[i][j];
            printf("%d ", &matrixAns[i][j]);
        }
    }
}