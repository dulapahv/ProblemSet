#include <iostream>

#include "Fleet.h"
#include "Vehicle.h"
#include "RegisteredVehicle.h"

using namespace std;

int main() {
	Vehicle* car1 = new Vehicle("Toyota", 20000, 2018);
	car1->print();

	RegisteredVehicle* car2 = new RegisteredVehicle("Toyota", 20000, 2018, "ABC123");
	car2->print();

	Fleet* fleet = new Fleet();
	fleet->addVehicle(*car1);
	fleet->addVehicle(*car2);
	fleet->calcCapitalCost();
	fleet->print();
	
	return 0;
}