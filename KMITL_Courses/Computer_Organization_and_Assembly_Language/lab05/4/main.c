#include <stdio.h>

#define N 5

int fib(int n)
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return fib(n - 1) + fib(n - 2);
}

int main()
{
	for (int i = 1; i <= N; i++)
		printf("%d ", fib(i));
	return 0;
}