#include <stdio.h>

#define ROW 6

int main() {
    char id[ROW][8];
    for (int i = 0; i < ROW; i++)
        for (int j = 0; j < 8; j++)
            scanf("%c", &id[i][j]);
    char name[ROW][8];
        for (int i = 0; i < ROW; i++)
            for (int j = 0; j < 8; j++)
                scanf("%c", &name[i][j]);            
    int sub1[ROW][6];
        for (int i = 0; i < ROW; i++)
            for (int j = 0; j < 6; j++)
                scanf("%c", &sub1[i][j]);
    char sub2[ROW][6];
        for (int i = 0; i < ROW; i++)
            for (int j = 0; j < 6; j++)
                scanf("%c", &sub2[i][j]);
    char sub3[ROW][4];
        for (int i = 0; i < ROW; i++)
            for (int j = 0; j < 6; j++)
                scanf("%c", &sub3[i][j]);
    
    float avgsub1 = 0, avgsub2 = 0, avgsub3 = 0;
    printf("a %d\n", sub1[1][0]);
    printf("b %d\n", sub1[1][1]);
    printf("c %d\n", sub1[1][2]);
    printf("d %d\n", sub1[1][3]);
}