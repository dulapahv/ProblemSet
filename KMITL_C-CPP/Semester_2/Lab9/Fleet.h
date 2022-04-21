#include <fstream>
#include <vector>

#include "Vehicle.h"

using namespace std;

class Fleet {
private:
	vector<Vehicle> asset_reg;
public:
	/** Fleet – default constructor
	 ** Create an empty fleet
	**/
	Fleet();
	/** Add a new vehicle to the fleet
	** /param v Vehicle a valid vehicle to be added
	** /return true if addition successful
	**/
	bool addVehicle(Vehicle v);
	/** Calculate fleet capital cost
	  *  /return double total capital cost
	**/
	double calcCapitalCost() {
		double sum = 0;
		for (int j = 0; j < asset_reg.size(); j++) {
			sum += asset_reg[j].getCost();
		}
		fprintf(stderr, "Total cost : % 10.2f\n", sum);
		return sum;
	}
	/** Print the asset register
	  *
  **/
	void print() {
		fprintf(stdout, "Asset Register\n");
		for (int j = 0; j < asset_reg.size(); j++) {
			asset_reg[j].print();
		}
	}
};
