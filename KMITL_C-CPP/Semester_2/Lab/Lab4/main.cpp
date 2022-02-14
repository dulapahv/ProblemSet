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
	vector<vector<Sub_District>> sub_districtGroup;
	vector<Sub_District> sub_district;
	string tempKey, tempName;
	double tempLatitude, tempLongitude, tempArea;
	long int tempPopulation;
	
	while (inFile >> tempKey >> tempName >> tempLatitude >> tempLongitude >> tempPopulation >> tempArea) {
		/* Store data according to the region type */
		const char* type = tempKey.c_str(); // Convert string to const char *
		if (strcmp(type, "Province") == 0) {
			province.push_back(Province(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
			sub_districtGroup.push_back(sub_district);
			sub_district.clear();
		}
		else if (strcmp(type, "Sub") == 0)
			sub_district.push_back(Sub_District(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
	}

	/* Push the last sub_district into sub_districtGroup */
	sub_districtGroup.push_back(sub_district);

	/* Remove the first index of a sub_districtGroup */
	sub_districtGroup.erase(sub_districtGroup.begin());

	/* Printing out result */
	cout << "============================================================" << endl;
	cout << "[Summary Of Population Density In Each Provinces And Districts]\n" << endl;
	cout << setprecision(9) << fixed;

	for (unsigned int i = 0; i < province.size(); i++) {
		cout << "Province " << province[i].getName() << setw(13) << '\t' << province[i].getPopulationDensity() << " people/sq.m." << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			cout << "- " << sub_districtGroup[i][j].getName() << setw(18) << '\t' << sub_districtGroup[i][j].getPopulationDensity() << " people/sq.m." << endl;
		cout << endl;
	}

	cout << "============================================================" << endl;
	cout << "[Summary Of Population In Each Provinces And Districts]\n" << endl;
	cout << setprecision(0);

    /* Compare the sum of population in province to the sum of population in sub_district */
    for (unsigned int i = 0; i < province.size(); i++) {
        double sum_province = 0;
        double sum_sub_district = 0;
        for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
            sum_sub_district += sub_districtGroup[i][j].getPopulation();
        sum_province += province[i].getPopulation();
        cout << "Province " << province[i].getName() << setw(13) << '\t' << province[i].getPopulation() << " people" << endl;
        for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
            cout << "- " << sub_districtGroup[i][j].getName() << setw(18) << '\t' << sub_districtGroup[i][j].getPopulation() << " people" << endl;
		cout << "Sum of population in districts: " << sum_sub_district << endl;
        cout << "Extra population from province: " << sum_province - sum_sub_district << " people." << endl;
        cout << endl;
    }

	inFile.close();
	return 0;
}