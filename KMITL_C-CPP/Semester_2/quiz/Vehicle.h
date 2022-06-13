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
	Vehicle(string name, double price) {
		this->name = name;
		this->price = price;
	};

	virtual double getCost() { return price; }
	virtual void print() {};
};


class RegisteredVehicle : public Vehicle {
protected:
	string reg_number;
public:
	RegisteredVehicle(string name, double price, string reg_number) : Vehicle(name, price) {
		this->reg_number = reg_number;
	}

	double getCost() {
		return price + 500;
	}
};


class Jet : public RegisteredVehicle {
private:
	double load_capacity;
	int max_passenger;
public:
	Jet(string name, double price, string reg_number) : RegisteredVehicle(name, price, reg_number) {
		load_capacity = 2000;
		max_passenger = 10;
	}

	void print();
};


class Car : public RegisteredVehicle {
private:
	double load_capacity;
	int max_passenger;
public:
	Car(string name, double price, string reg_number) : RegisteredVehicle(name, price, reg_number) {
		load_capacity = 1000;
		max_passenger = 4;
	}

	void print();
};


class Bicycle : public Vehicle {
private:
	int seats;
	bool hasBasket;
public:
	Bicycle(string name, double price) : Vehicle(name, price) {
		seats = 2;
		hasBasket = true;
	}

	void print();
};


#endif //VEHICLE_H
