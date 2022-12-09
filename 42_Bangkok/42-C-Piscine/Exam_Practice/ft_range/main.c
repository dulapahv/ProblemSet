#include "ft_range.c"
#include <stdio.h>

int main() {
	int	*arr = ft_range(0, -3);
	for (int i = 0; i < 4; i++)
		printf("%d, ", arr[i]);
}
