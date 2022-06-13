// Timing Example

#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>

#include "Point3D.h"
#include "Point4D.h"

#include "DivideByZeroException.h"
#include "OverflowException.h"
#include "Elapsed.h"

const long int n = 100000000;

int main()
{
	fprintf(stdout, "Timimg test %d iterations\n", n);
	fprintf(stdout, "\n3D point\n");
	double t0 = elapsed();
	double x, y, z;
	x = y = z = 0.0;
	for (long int j = 0; j < n; j++) {
		Point3D(x, y, z);
		x = x + 0.1;
	}
	double dt = elapsed();
	// double dt = t1 - t0;
	fprintf(stderr, "Time %10.3f s  %d iterations, %10.3f ns/constructor\n",
		dt, n, (dt * 1.0e9) / (double)n);

	fprintf(stdout, "\n4D point\n");
	double z4;
	elapsed();
	x = y = z = z4 = 0.0;
	for (long int j = 0; j < n; j++) {
		Point4D(x, y, z, z4);
		x = x + 0.1;
	}
	dt = elapsed();
	// double dt = t1 - t0;
	fprintf(stderr, "Time %10.3f s  %d iterations, %10.3f ns/constructor\n",
		dt, n, (dt * 1.0e9) / (double)n);
}

