#include "ft_ultimate_range.c"
#include <stdio.h>

int main() {
	int *arr;
	int range;

	range = ft_ultimate_range(&arr, -5, 8);
	printf("%d\n", range);
	for (int i = 0; i < range; i++)
		printf("%d ", arr[i]);
}
