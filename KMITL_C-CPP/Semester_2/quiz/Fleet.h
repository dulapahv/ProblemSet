#ifndef FLEET_H
#define FLEET_H

#include <vector>

#include "Vehicle.h"

class Fleet {
private: 
	vector<Vehicle*> asset_reg;
public: 
	Fleet() {};

	bool addVehicle(Vehicle* v);

	double calcVehicleCost();

	void print();
};

#endif //FLEET_H