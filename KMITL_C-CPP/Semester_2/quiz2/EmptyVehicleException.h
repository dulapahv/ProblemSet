#ifndef EMPTY_VEHICLE_EXCEPTION
#define EMPTY_VEHICLE_EXCEPTION

#include <iostream>
#include <stdexcept>

using namespace std;

//user defined class for handling exception

class EmptyVehicleException : public runtime_error {
public:
	EmptyVehicleException()
		: runtime_error("Error: Vehicle list cannot be empty!\n") {
	}
};

#endif  // EMPTY_VEHICLE_EXCEPTION