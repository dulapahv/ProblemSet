#include "ft_strcat.c"
#include <stdio.h>

int main() {
	char src[20] = "World!";
	char dest[] = "Hello ";
	printf("%s", ft_strcat(dest, src));
}
