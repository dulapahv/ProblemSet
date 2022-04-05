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
    PointND<T> operator+(PointND<T>& p);

    /* - operator method */
    PointND<T> operator-(PointND<T>& p);

    /* * operator method */
    PointND<T> operator*(PointND<T>& p);

    /* / operator method */
    PointND<T> operator/(PointND<T>& p);

    unsigned int size();

    void print(ofstream& f);
	void print();
};
