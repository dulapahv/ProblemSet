#pragma once

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception

class QuadrantException : public runtime_error {
public:
	QuadrantException()
		: runtime_error("Quadrant error: Point is not in the first quadrant and/or in the specified limit\n") {
	}
};
