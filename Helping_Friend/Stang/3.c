#include <stdio.h>

int main(void)
{
	int isPrime[] = {
		0, // this is [0]
		0, 1, 1, 0, 1, 0, 1, 0, 0, 0,
		// elements [2], [3], [5], [7] are true because 2, 3, 5 and 7 are primes
		1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
		// elements [12], [14], [15], [16], [18], [20] are false because they are composites
		0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
		1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
		1, 0, 1, 0, 0, 0, 1, 0, 0, 0,
		0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
		1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
		1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
		0, 0, 0, 0, 0, 0, 1, 0, 0, 0};

	int a, b;

	scanf("%d", &a);
	scanf("%d", &b);

	printf("[%d, %d]: ", a, b);

	int index = a;
	int count = 0;
	// /*
	// The idea is: Size of array / Size of an element = length of array

	// sizeof(isPrime) is the size of the array
	// sizeof(isPrime[0]) is the size of an element

	// So, sizeof(isPrime)/sizeof(isPrime[0]) will give length of the array.
	// */
	// int size = sizeof(isPrime) / sizeof(isPrime[0]);

	// while (index < size && index <= b) {
	// 	if (isPrime[index] == 1) {
	// 		count++;
	// 		printf("%d ", index);
	// 	}
	// 	index++;
	// }

	// printf("(%d)", count);

	// return 0;
	
	while (index <= b) {
		if (isPrime[index] == 1) {
			count++;
			printf("%d ", index);
		}
		index++;
	}

	printf("(%d)", count);

	return 0;
}
