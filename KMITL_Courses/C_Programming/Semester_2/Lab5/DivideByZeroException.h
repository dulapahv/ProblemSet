#pragma once

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception
class Exception : public runtime_error {
public:
	Exception()
		: runtime_error("Math error: Attempted to divide by Zero\n") {
	}
};