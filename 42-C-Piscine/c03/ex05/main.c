#include "ft_strlcat.c"
#include <stdio.h>
#include <string.h>

int main() {
	char first[] = "Our love is like a pi, ";
	char last[] = "it never ends <3";
	int r;
	int size = 30;
	char buffer[size];

	strcpy(buffer, first);
	r = strlcat (buffer, last, size);
	
	/*
	 * The ft_strlcat returns the length of first string + last string
	 * However, it only concatenate the string according to the size you gave it.
	 * size = 30 means that it just copies the first 30 char of first + last string.
	 *
	 */

	printf("%s\n", buffer);
	printf("Value returned: %d\n", r);

	if (r > size)
		printf("String truncated\n");
	else
		printf("String was fully copied\n");
}
