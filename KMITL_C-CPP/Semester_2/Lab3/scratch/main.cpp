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
		else if (strcmp(type, "Town") == 0) {
			town.push_back(Town(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
		}
	}
	/* Push the last sub_district and town vector into sub_districtGroup and townGroup vector */
	sub_districtGroup.push_back(sub_district);
	townGroup.push_back(townSubGroup);
	townSubGroup.push_back(town);

	/* Remove the first index of a sub_districtGroup and townGroup vector */
	sub_districtGroup.erase(sub_districtGroup.begin());
	townSubGroup.erase(townSubGroup.begin()+3);
	townGroup.erase(townGroup.begin());

	/* Prevent auto conversion of output number to exponential */
	cout << setprecision(12);

	/*** DEBUG ***/
	///* Get name of each province, sub-district, and town */
	//cout << "\nProvince:" << endl;
	//for (unsigned int i = 0; i < province.size(); i++)
	//	cout << province[i].getName() << endl;
	//cout << "\nSub-District:" << endl;
	//for (unsigned int i = 0; i < sub_district.size(); i++)
	//	cout << sub_district[i].getName() << endl;
	//cout << "\nTown:" << endl;
	//for (unsigned int i = 0; i < town.size(); i++)
	//	cout << town[i].getName() << endl;

	///* Get sum of population in each province, sub-district, and town */
	//double sumProvince = 0, sumSub = 0, sumTown = 0;
	//for (unsigned int i = 0; i < province.size(); i++)
	//	sumProvince += province[i].getPopulation();
	//for (unsigned int i = 0; i < sub_district.size(); i++)
	//	sumSub += sub_district[i].getPopulation();
	//for (unsigned int i = 0; i < town.size(); i++)
	//	sumTown += town[i].getPopulation();

	//cout << "\nSum Province: " << sumProvince << endl;
	//cout << "Sum Sub-District: " << sumSub << endl;
	//cout << "Sum Town: " << sumTown << endl;

	///* Get area of each province, sub-district, and town */
	//double sumProvinceArea = 0, sumSubArea = 0, sumTownArea = 0;
	//for (unsigned int i = 0; i < province.size(); i++)
	//	sumProvinceArea += province[i].getArea();
	//for (unsigned int i = 0; i < sub_district.size(); i++)
	//	sumSubArea += sub_district[i].getArea();
	//for (unsigned int i = 0; i < town.size(); i++)
	//	sumTownArea += town[i].getArea();

	//cout << "\nProvince Area: " << sumProvinceArea << endl;
	//cout << "Sub-District Area: " << sumSubArea << endl;
	//cout << "Sum Town Area: " << sumTownArea << endl;

	///* Get population density of each province, sub-district, and town */
	//cout << "\nProvince population density:" << endl;
	//for (unsigned int i = 0; i < province.size(); i++)
	//	cout << province[i].getName() << ": " << province[i].getPopulationDensity() << endl;
	//cout << "\nSub-District population density:" << endl;
	//for (unsigned int i = 0; i < sub_district.size(); i++)
	//	cout << sub_district[i].getName() << ": " << sub_district[i].getPopulationDensity() << endl;
	//cout << "\nTown population density:" << endl;
	//for (unsigned int i = 0; i < town.size(); i++)
	//	cout << town[i].getName() << ": " << town[i].getPopulationDensity() << endl;

	///* Display population density of each province, sub-district, and town */
	//for (unsigned int i = 0; i < province.size(); i++)
	//	cout << "Province " << province[i].getName() << setw(10) << '\t' << province[i].getPopulationDensity() << endl;
	//for (unsigned int i = 0; i < sub_district.size(); i++)
	//	cout << "- " << sub_district[i].getName() << setw(10) << '\t' << sub_district[i].getPopulationDensity() << endl;
	//for (unsigned int i = 0; i < town.size(); i++)
	//	cout << "\t- " << town[i].getName() << setw(10) << '\t' << town[i].getPopulationDensity() << endl;
	/*** DEBUG ***/

	/* Main program part */
	for (unsigned int i = 0; i < province.size(); i++) {
		cout << "Province " << province[i].getName() << setw(13) << '\t' << province[i].getPopulationDensity() << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++) {
			cout << "- " << sub_districtGroup[i][j].getName() << setw(18) << '\t' << sub_districtGroup[i][j].getPopulationDensity() << endl;
			for (unsigned int k = 0; k < townGroup[i][j].size(); k++) {
				cout << "\t- " << townGroup[i][j][k].getName() << setw(10) << '\t' << townGroup[i][j][k].getPopulationDensity() << endl;
				cout << i << j << k;
			}	
		}
		cout << endl;
	}

	inFile.close();
	return 0;
}