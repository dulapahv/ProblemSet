#ifndef RUSH01_H
#define RUSH01_H

void ft_putstr(char *str);
void ft_putchar(char c);
int is_input_valid(char *str, int size, int *arr);
void fill_1(int grid[4][4], int *top, int *bottom, int *left, int *right);
void fill_4(int grid[4][4], int *top, int *bottom, int *left, int *right);
int ft_is_num(char c);

#endif