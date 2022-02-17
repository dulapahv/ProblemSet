// ExampleA.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "Rectangle.h"
#include "Complex.h"
#include "Point.h"
#include <vector> // for vectors


const int n_max = 10000;

int main()
{
    std::vector<Rectangle> vr;
    Point p1, p2;
    p1 = Point(1.0, 1.0);
    p2 = Point(2.0, 4.0);
    Rectangle ra(p1, p2);

    std::cout << "Make a vector " << std::endl;

    size_t n_current = vr.size();
    size_t n_cap = vr.capacity();
    size_t max_size = 0;
    std::cout << "Init elem " << n_current << " cap " << n_cap << std::endl;
    //for (int j = 0; j < n_max; j++) {
    //    // Add some code here to show us how vector allocates space on YOUR computer!!
    //}
    //// Print some conclusions here .. how many extra elements are added
    //// whenever the vector becomes full

    //// Try using reserve here to see what happens?  Can you adjust the
    //// extra space allocated ??
    //for (int j = 0; j < n_max; j++) {
    //    // Now show us how vector allocates space on YOUR computer after reserve
    //}

}


