#include <stdio.h>

int main() {
	// calculate dot product of n dimensions
	int n;
	scanf("%d", &n);

	double a[n], b[n];
	
	for (int i = 0; i < n; i++) {
		scanf("%lf", &a[i]);
	}

	for (int i = 0; i < n; i++) {
		scanf("%lf", &b[i]);
	}

	double dotProduct = 0.0;
	for (int i = 0; i < n; i++) {
		dotProduct += a[i] * b[i];
	}
	
	printf("Dot product = %.2lf", dotProduct);
}