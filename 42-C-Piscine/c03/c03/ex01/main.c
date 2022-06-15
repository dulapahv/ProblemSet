#include "ft_strncmp.c"
#include <stdio.h>

int main() {
	char str[] = "Hellog";
	char str2[] = "Hello";
	printf("%d", ft_strncmp(str, str2, 6));
}
