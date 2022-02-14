#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include "Region.h"

#define INFILE "input.txt"
#define OUTFILE "output.txt"

using namespace std;

int main() {
	/* Reads input file */
	ifstream inFile(INFILE);

	/* Move file pointer to the next line */
	inFile.ignore(256, '\n');

	/* Store read data in vector */
	vector<Province> province;
	vector<Sub_District> sub_district;
	vector<Town> town;
	string tempKey, tempName;
	double tempLatitude, tempLongitude, tempPopulation, tempArea;

	vector<vector<Sub_District>> sub_districtGroup;
	vector<vector<vector<Town>>> townGroup;
	vector<vector<Town>> townSubGroup;
	
	while (inFile >> tempKey >> tempName >> tempLatitude >> tempLongitude >> tempPopulation >> tempArea) {
		/* Store data according to the region type */
		const char* type = tempKey.c_str(); // Convert string to const char *
		if (strcmp(type, "Province") == 0) {
			province.push_back(Province(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
			sub_districtGroup.push_back(sub_district);
			sub_district.clear();
			townGroup.push_back(townSubGroup);
			townSubGroup.clear();
		}
		else if (strcmp(type, "Sub") == 0) {
			sub_district.push_back(Sub_District(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
			townSubGroup.push_back(town);
			town.clear();
		}
	}
	/* Push the last sub_district and town vector into sub_districtGroup and townGroup vector */
	sub_districtGroup.push_back(sub_district);

	/* Remove the first index of a sub_districtGroup and townGroup vector */
	sub_districtGroup.erase(sub_districtGroup.begin());

	/* Round number */
	cout << setprecision(9) << fixed;

	/* Main program part */
	for (unsigned int i = 0; i < province.size(); i++) {
		cout << "Province " << province[i].getName() << setw(13) << '\t' << province[i].getPopulationDensity() << " people/sq.m." << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			cout << "- " << sub_districtGroup[i][j].getName() << setw(18) << '\t' << sub_districtGroup[i][j].getPopulationDensity() << " people/sq.m." << endl;
		cout << endl;
	}

	inFile.close();
	return 0;
}