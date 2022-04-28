#ifndef REGISTEREDVEHICLE_H
#define REGISTEREDVEHICLE_H

#include "Vehicle.h"

class RegisteredVehicle : public Vehicle {
protected:
	string reg_number;
public:
	/** RegisteredVehicle - Constructor taking additional reg_number parameter **/
	RegisteredVehicle(string name, double price, string reg_number) : Vehicle(name, price) {
		this->reg_number = reg_number;
	}

	// double getCost();
};

#endif  // REGISTEREDVEHICLE_H