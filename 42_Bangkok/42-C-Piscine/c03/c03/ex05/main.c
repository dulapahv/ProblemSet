#include "ft_strlcat.c"
#include <stdio.h>

int main() {
	char src[] = "World!";
	char dest[20] = "Hello ";
	printf("%d\n", ft_strlcat(dest, src, 12));
	printf("%s\n", dest);
}
