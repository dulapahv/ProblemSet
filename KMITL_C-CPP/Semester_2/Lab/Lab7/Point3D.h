/** Point3D class **/

#include <iostream>
#include "math.h"

using namespace std;

#include "Point.h"

class Point3D : public Point {
private:
	double z;
public:
	Point3D(double x, double y, double z) : Point(x, y) {
		this->z = z;
	}

	void print(ofstream& f);
	void print();
};

