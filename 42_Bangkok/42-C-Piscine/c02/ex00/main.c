#include "ft_strcpy.c"
#include <stdio.h>

int main()
{
	char src[] = "Hello";
	char dest[10];

	ft_strcpy(dest, src);
	printf("%s", dest);
}
