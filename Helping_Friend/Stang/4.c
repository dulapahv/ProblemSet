#include <stdio.h>

int main() {
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);

	printf("[%d, %d]: ", a, b);

	int count = 0;
	int i = a;
	while (i <= b) {
		int isPrime = 1;
		int j = 2;
		while (j < i) {
			if (i % j == 0) {
				isPrime = 0;
				break;
			}
			j++;
		}

		if (isPrime == 1) {
			count++;
			printf("%d ", i);
		}
		i++;
	}

	printf("(%d)", count);

	return 0;
}