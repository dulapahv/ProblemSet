#ifndef FLEET_H
#define FLEET_H

#include <vector>

#include "Vehicle.h"

class Fleet {
private: 
	vector<Vehicle*> asset_reg;
public: 
	/** Fleet – default constructor
	 ** Create an empty fleet
	**/
	Fleet() {};
	/** Add a new vehicle to the fleet
	** /param v Vehicle a valid vehicle to be added
	** /return true if addition successful
	**/
	bool addVehicle(Vehicle* v);
	/** Calculate fleet capital cost * /return double total capital cost **/
	double calcCapitalCost();

	/** Print the asset register **/
	void print();
};

#endif //FLEET_H