#include "ft_range.c"
#include <stdio.h>

int main() {
	int *arr = ft_range(-5, 8);
	for (int i = 0; i < 13; i++) // Don't forget to change number of loops!
		printf("%d ", arr[i]);
}
