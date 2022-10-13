#include <stdio.h>
#include <stdlib.h>

int main() {
	// calculate dot product of n dimensions
	int n;
	scanf("%d", &n);

	int *a = malloc(n * sizeof(int));
	int *b = malloc(n * sizeof(int));

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}

	for (int i = 0; i < n; i++) {
		scanf("%d", &b[i]);
	}

	double dotProduct = 0.0;
	for (int i = 0; i < n; i++) {
		dotProduct += a[i] * b[i];
	}

	printf("Dot product = %.2lf", dotProduct);

	free(a);
	free(b);
}