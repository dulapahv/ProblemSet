#pragma once

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception

class DivideByZeroException : public runtime_error {
public:
	DivideByZeroException()
		: runtime_error("Math error: Attempted to divide by Zero\n") {
	}
};
