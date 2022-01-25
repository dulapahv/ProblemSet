#pragma once

class Triangle {
private:
    double x1, y1, x2, y2, x3, y3;
public:
    Triangle();
    Triangle(double a1, double b1, double a2, double b2, double a3, double b3);

    double perimeter();
    double Area();

    bool isEquilateral();
    bool isIsosceles();
    bool isScalene();
};