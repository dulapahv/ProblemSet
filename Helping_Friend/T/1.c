#include <stdio.h>
#include <stdlib.h>

int main() {
	double s, v, a_m, a_km, t;

	printf("Enter velocity in km/hr: ");
	scanf("%lf", &v);
	printf("Enter distance s in meters: ");
	scanf("%lf", &s);

	v = v * 1000 / 3600;
	t = (2 * s) / v;
	printf("Time to take off is\t%.3lf second(s).\n", t);

	a_m = v / t;
	a_km = a_m * 3600 / 1000;
	printf("Acceleration is\t%.3lf m/s^2\n\t\tor %.3lf km/hr^2\n", a_m, a_km);

	printf("End of Program\n");
	system("pause");
	return 0;
}