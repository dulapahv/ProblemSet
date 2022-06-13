#pragma once

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception

class OverflowException : public runtime_error {
public:
	OverflowException()
		: runtime_error("Math error: Stack overflow\n") {
	}
};
