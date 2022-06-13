/** Point3D class **/

#include <iostream>
#include "math.h"

using namespace std;

#include "Point3D.h"

void Point3D::print(ofstream& f) {
	f << '(' << getX() << ',' << getY() << ',' << z << ')';
}
void Point3D::print() {
	cout << '(' << getX() << ', ' << getY() << ', ' << z << ')';
}

