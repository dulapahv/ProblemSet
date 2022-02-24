#pragma once

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception
class OverflowException : public runtime_error {
public:
    OverflowException()
        : runtime_error("Overflow Error: Point not in a unit circle.\n") {
    }
    OverflowException(double limit)
        : runtime_error("Overflow Error: Point not in a unit circle. \n") {
        this->limit = limit;
    }
private:
    double limit;
};