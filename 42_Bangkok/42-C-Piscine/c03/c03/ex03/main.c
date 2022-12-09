#include "ft_strncat.c"
#include <stdio.h>

int main() {
	char src[20] = "World!";
	char dest[] = "Hello ";
	printf("%s", ft_strncat(dest, src, 12));
}
