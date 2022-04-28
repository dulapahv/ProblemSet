#ifndef VEHICLE_H
#define VEHICLE_H

#include <iostream>
#include <string>

using namespace std;

class Vehicle {
protected:
	string name;
	double price;
	double multiplier;
public:
	/** Vehicle - Constructor taking name and price **/
	Vehicle(string name, double price) {
		this->name = name;
		this->price = price;
	};

	/** Abstract method for all child class **/
	virtual double getCost() { return price * multiplier; }
	virtual void print() {};
};

#endif //VEHICLE_H
