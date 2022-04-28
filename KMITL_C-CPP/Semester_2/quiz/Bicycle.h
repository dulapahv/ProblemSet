#ifndef BICYCLE_H
#define BICYCLE_H

#include "Vehicle.h"

class Bicycle : public Vehicle {
private:
	int seats;
	bool hasBasket;
	double multiplier = 1.1;
public:
	Bicycle(string name, double price) : Vehicle(name, price) {
		seats = 2;
		hasBasket = true;
	}

	double getCost();

	void print() {
		cout << "Bicycle: " << name << " Seats: " << seats << " Basket: " << hasBasket << endl;
	}
};

#endif  // BICYCLE_H