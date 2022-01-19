#pragma once

#include "Point.h"

using namespace std;

class Triangle {
private:
	Point p1, p2, p3;
public:
	Triangle(Point p1, Point p2, Point p3);
	Triangle(float p1, float p2, float p3);

	Triangle(Triangle* original, float scale = 1.0f);
	Triangle(Triangle* original, float rot = 0.0, float scale = 1.0f);

	Point getp1();
	Point getp2();
	Point getp3();

	float getArea();
	float getPerimeter();

	bool isIsosceles();
	bool isEqualateral();
};
