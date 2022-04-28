#ifndef CAR_H
#define CAR_H

#include "RegisteredVehicle.h"

class Car : public RegisteredVehicle {
private:
	double load_capacity;
	int max_passenger;
    double multiplier = 1.25;
public:
	Car(string name, double price, string reg_number) : RegisteredVehicle(name, price, reg_number) {
		load_capacity = 1000;
		max_passenger = 4;
	}

    double getCost();

	void print() {
		cout << "Car: " << name << " Load : " << load_capacity << " Passenger : " << max_passenger << endl;
	}
};

#endif  // CAR_H