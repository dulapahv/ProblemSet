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
	/* Reads input file and store data in vector */
	ifstream inFile(INFILE);

	inFile.ignore(256, '\n');  // Move file pointer to the next line

	vector<Province> province;
	vector<vector<Sub_District>> sub_districtGroup;
	vector<Sub_District> sub_district;
	string tempKey, tempName;
	double tempLatitude, tempLongitude, tempArea;
	long int tempPopulation;

	while (inFile >> tempKey >> tempName >> tempLatitude >> tempLongitude >> tempPopulation >> tempArea) {
		// Store data according to the region type
		if (tempKey.compare("Province") == 0) {
			province.push_back(Province(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
			sub_districtGroup.push_back(sub_district);
			sub_district.clear();
		}
		else if (tempKey.compare("Sub") == 0)
			sub_district.push_back(Sub_District(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
	}

	sub_districtGroup.push_back(sub_district);  // Push the last sub_district into sub_districtGroup vector
	sub_districtGroup.erase(sub_districtGroup.begin());  // Remove the first index of a sub_districtGroup vector

	/* Compute and output statistics to a file */
	ofstream outFile(OUTFILE);

	outFile << "============================================================" << endl;
	outFile << "[Summary Of Population Density In Each Provinces And Districts]\n" << endl;
	outFile << setprecision(9) << fixed;

	for (unsigned int i = 0; i < province.size(); i++) {
		outFile << "Province " << province[i].getName() << setw(43 - province[i].getName().length()) << province[i].getPopulationDensity() << " people/sq.m." << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			outFile << "- " << sub_districtGroup[i][j].getName() << setw(50 - sub_districtGroup[i][j].getName().length()) << sub_districtGroup[i][j].getPopulationDensity() << " people/sq.m." << endl;
		outFile << endl;
	}

	outFile << "============================================================" << endl;
	outFile << "[Summary Of Population In Each Provinces And Districts]\n" << endl;
	outFile << setprecision(0);

	// Compare the sum of population in province to the sum of population in sub_district
	for (unsigned int i = 0; i < province.size(); i++) {
		double sum_province = 0;
		double sum_sub_district = 0;

		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			sum_sub_district += sub_districtGroup[i][j].getPopulation();
		sum_province += province[i].getPopulation();

		outFile << "Province " << province[i].getName() << setw(43 - province[i].getName().length()) << province[i].getPopulation() << " people" << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			outFile << "- " << sub_districtGroup[i][j].getName() << setw(50 - sub_districtGroup[i][j].getName().length()) << sub_districtGroup[i][j].getPopulation() << " people" << endl;
		outFile << "Extra population from province: " << sum_province - sum_sub_district << " people" << endl;
		outFile << endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}