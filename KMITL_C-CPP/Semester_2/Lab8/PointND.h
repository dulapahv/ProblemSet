/** PointND class **/

#pragma once

#include <iostream>
#include <vector>

using namespace std;

template <typename T>
class PointND {
private:
    unsigned int nd;
    vector<T> x;
public:
    static int XLIMIT;
    static int YLIMIT;

    PointND(vector<T> x) {
        this->nd = x.size();
        this->x.resize(nd);
        for (int i = 0; i < nd; i++) {
            this->x[i] = x[i];
        }
    }

    /* + operator method */
    PointND<T> operator+(PointND<T>& p);  // Element-wise addition
    PointND<T> operator+(T a);  // Scalar addition

    /* - operator method */
    PointND<T> operator-(PointND<T>& p);  // Element-wise subtraction
    PointND<T> operator-(T a);  // Scalar subtraction

    /* * operator method */
    PointND<T> operator*(PointND<T>& p);  // Element-wise multiplication
    PointND<T> operator*(T a);  // Scalar multiplication

    /* / operator method */
    PointND<T> operator/(PointND<T>& p);  // Element-wise division
    PointND<T> operator/(T a);  // Scalar division

    unsigned int size();

    void print(ofstream& f);
	void print();
};
