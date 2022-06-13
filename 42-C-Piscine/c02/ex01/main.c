#include "ft_strncpy.c"
#include <stdio.h>

int main() {
	char src[] = "Hello World!";
	char dest[12];

	ft_strncpy(dest, src, 12);
	printf("%s", dest);
}
