#include <stdio.h>

int main()
{
	int i = 1;
	while (i > 0)
	{
		i = i + 1;
		if (i < 0)
		{
			printf("i was %d before\n", i - 1);
			printf("i is %d now\n", i);
		}
	}
	return 0;
}