#pragma once

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception

class UnderflowException : public runtime_error {
public:
	UnderflowException()
		: runtime_error("Math error: Stack underflow\n") {
	}
};
