#pragma once

class Triangle {
private:
	double p1x, p1y, p2x, p2y, p3x, p3y;
public:
	Triangle(double p1x, double p1y, double p2x, double p2y, double p3x, double p3y);
	Triangle(double p1[2], double p2[2], double p3[2]);

	double getp1x(); double getp1y();
	double getp2x(); double getp2y();
	double getp3x(); double getp3y();

	double getArea();
	double getPerimeter();

	bool isEquilateral();
	bool isIsosceles();
	bool isScalene();
};
