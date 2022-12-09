#include "Fleet.h"

int main() {
	Bicycles bicycles1("Bicycles1", 500);
	Bicycles bicycles2("Bicycles2", 300);
	Truck truck1("Truck1", 4999, "PI3141");
	Truck truck2("Truck2", 5999, "TAO6283");
	Fleet fleet1 = Fleet();

	fleet1.addVehicle(&bicycles1);
	fleet1.addVehicle(&bicycles2);
	fleet1.addVehicle(&truck1);
	fleet1.addVehicle(&truck2);
	fleet1.calcCapitalCost();
	fleet1.print();
}