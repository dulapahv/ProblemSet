#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ft_strnstr.c"
#include "ft_strlen.c"

int main() {
	printf("%s", ft_strnstr("aaabcabcd", "abcd", 9));
}