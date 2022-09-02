#include <stdio.h>

int main() {
	unsigned int i = -1;
	while (i > 0)
	{
		i = i - 1;
		if (i == 0)
		{
			printf("i was %10u before\n", i + 1);
			printf("i was %10u before\n", i);
		}
	}
	return 0;
}