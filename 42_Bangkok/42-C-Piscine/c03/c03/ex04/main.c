#include "ft_strstr.c"
#include <stdio.h>

int main() {
	char str[] = "Our love is like a pi, it never ends.";
	char to_find[] = "love";
	char *ptr = ft_strstr(str, to_find);
	while (*ptr) {
		printf("%c", *ptr++);
	}
}
