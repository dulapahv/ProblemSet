/** Point3D class **/

#include <iostream>
#include "math.h"

using namespace std;

#include "Point3D.h"

class Point4D : public Point3D {
private:
	double z4;
public:
	Point4D(double x, double y, double z, double z4) : Point3D(x, y, z) {
		this->z4 = z4;
	}

	void print(ofstream& f);
	void print();
};

