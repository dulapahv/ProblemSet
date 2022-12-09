#include "ft_strjoin.c"
#include <stdio.h>

int	main() {
	char **strs;
	char *separator;
	char *result;

	strs = (char**)malloc(4 * sizeof(strs));
	strs[0] = "Love will guide the way, our hearts bound by an eternal promise!";
	strs[1] = "We share our smile, our words unspoken.";
	strs[2] = "Our love will be one of respect, trust, and confidence forever.";
	strs[3] = "From this day forth, our fates are bound together.";
	separator = " ";
	result = ft_strjoin(4, strs, separator);
	printf("%s\n", result);
	free(result);
}
