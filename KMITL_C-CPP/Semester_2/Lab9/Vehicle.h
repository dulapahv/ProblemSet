#ifndef VEHICLE_H
#define VEHICLE_H

#include <iostream>
#include <string>

using namespace std;

class Vehicle {
protected:
	string name;
	double price;
public:
	/** Vehicle - Constructor taking name and price **/
	Vehicle(string name, double price) {
		this->name = name;
		this->price = price;
	};

	/** Abstract method for all child class **/
	virtual double getCost() { return price; }
	virtual void print() {};
};


class RegisteredVehicle : public Vehicle {
protected:
	string reg_number;
public:
	/** RegisteredVehicle - Constructor taking additional reg_number parameter **/
	RegisteredVehicle(string name, double price, string reg_number) : Vehicle(name, price) {
		this->reg_number = reg_number;
	}

	/** getCost - return price + registration fee (assuming fee is fixed) **/
	double getCost() {
		return price + 500;
	}
};


class Truck : public RegisteredVehicle {
private:
	/** Attributes **/
	double  load_capacity;
	int max_passenger;
public:
	Truck(string name, double price, string reg_number) :RegisteredVehicle(name, price, reg_number) {
		load_capacity = 2000;
		max_passenger = 15;
	}

	/** print details (name, load, max_passenger, and headlight) **/
	void print() {
		cout << "Truck: " << name << " Load : " << load_capacity << " Passenger : " << max_passenger << endl;
	}
};


class Bicycles : public Vehicle {
private:
	/** Attributes **/
	int seats;
	bool hasBasket;
public:
	Bicycles(string name, double price) : Vehicle(name, price) {
		seats = 2;
		hasBasket = true;
	}
	/** print details (name, seats, and basket) **/
	void print() {
		cout << "Bicycles: " << name << " Seats: " << seats << " Basket: " << hasBasket << endl;
	}
};

#endif //VEHICLE_H
