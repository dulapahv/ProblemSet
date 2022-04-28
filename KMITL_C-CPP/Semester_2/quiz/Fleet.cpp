#include "Fleet.h"

bool Fleet::addVehicle(Vehicle* v) {
    asset_reg.push_back(v);
	return (1);
}

double Fleet::calcCapitalCost() {
	double sum = 0.0;

	for (int j = 0; j < asset_reg.size(); j++) {
		sum += asset_reg[j]->getCost();
	}

	fprintf(stderr, "Total cost: %10.2f\n", sum);
	return (sum);
}

void Fleet::print() {
	fprintf(stdout, "Asset Register\n");

	for (int j = 0; j < asset_reg.size(); j++) {
		asset_reg[j]->print();
	}
}