#ifndef JET_H
#define JET_H

#include "RegisteredVehicle.h"

class Jet : public RegisteredVehicle {
private:
	double load_capacity;
	int max_passenger;
    double multiplier = 1.5;
public:
	Jet(string name, double price, string reg_number) : RegisteredVehicle(name, price, reg_number) {
		load_capacity = 2000;
		max_passenger = 10;
	}

    double getCost();

	void print() {
		cout << "Jet: " << name << " Load : " << load_capacity << " Passenger : " << max_passenger << endl;
	}
};

#endif  // JET_H