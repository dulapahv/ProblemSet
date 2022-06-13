#include <math.h>
#include <assert.h>
#include "Triangle.h"

using namespace std;

double Euclidean(double x1, double y1, double x2, double y2) {
    double EU = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    return EU;
}

Triangle::Triangle() {
    x1 = 1;
    y1 = 1;
    x2 = 2;
    y2 = 2;
    x3 = 3;
    y3 = 3;
}

Triangle::Triangle(double a1, double b1, double a2, double b2, double a3, double b3) {
    x1 = a1;
    y1 = b1;
    x2 = a2;
    y2 = b2;
    x3 = a3;
    y3 = b3;
}

double Triangle::perimeter() {
    double E1 = Euclidean(x1, y1, x2, y2);
    double E2 = Euclidean(x2, y2, x3, y3);
    double E3 = Euclidean(x3, y3, x1, y1);
    return E1 + E2 + E3;
}

double Triangle::Area() {
    double h = perimeter() / 2;
    double s1 = Euclidean(x1, y1, x2, y2);
    double s2 = Euclidean(x2, y2, x3, y3);
    double s3 = Euclidean(x3, y3, x1, y1);
    double a = sqrt(h * (h - s1) * (h - s2) * (h - s3));
    return a;
}

bool Triangle::isEquilateral() {
    double E1 = Euclidean(x1, y1, x2, y2);
    double E2 = Euclidean(x2, y2, x3, y3);
    double E3 = Euclidean(x3, y3, x1, y1);
    if (E1 == E2 && E2 == E3) {
        return true;
    }
    else {
        return false;
    }
}

bool Triangle::isIsosceles() {
    double E1 = Euclidean(x1, y1, x2, y2);
    double E2 = Euclidean(x2, y2, x3, y3);
    double E3 = Euclidean(x3, y3, x1, y1);
    if (E1 == E2 || E2 == E3 || E1 == E3) {
        return true;
    }
    else {
        return false;
    }
}

bool Triangle::isScalene() {
    double E1 = Euclidean(x1, y1, x2, y2);
    double E2 = Euclidean(x2, y2, x3, y3);
    double E3 = Euclidean(x3, y3, x1, y1);
    if (E1 != E2 && E2 != E3 && E1 != E3) {
        return true;
    }
    else {
        return false;
    }
}