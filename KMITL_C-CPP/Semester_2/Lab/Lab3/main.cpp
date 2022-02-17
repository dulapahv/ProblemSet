#include <assert.h>
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
	/** Read input file and store data in vector **/
	ifstream inFile(INFILE);
	assert(inFile);  // Check whether input file is accessible or not

	vector<Province> province;
	vector<vector<Sub_District>> sub_districtGroup;
	vector<Sub_District> sub_district;
	string tempKey, tempName;
	double tempLatitude, tempLongitude, tempArea;
	long long int tempPopulation;

	inFile.ignore(256, '\n');  // Move file pointer to the next line

	/*
	Algorithm:

	1. While it is not EOF, read the data according to the space separated column <name><lat long><population><area sq m> and store them into the temporary variables.
	2. Determine the type of region using a temporary variable that holds the key value.
	3. If it is a "Province", create a Province object using the data from the temporary variables and add it to the province vector.
	4. If it is a "Sub" (sub-district), create a Sub_District object using the data from the temporary variables, then add it to the sub_district vector.
	5. Since there could be more than 1 sub-district in each province, if the new read data (<key>) is "Sub", then go to number 4. But if the new read data is
	   is "Province", then add the sub_district vector (which contains all the sub-districts in each province) into the sub_districtGroup vector.
	   Now, sub_districtGroup vector is acting like a 2D array storing the index of provinces that contain sub-districts, and each of them stores
	   each sub-district's data.
	6. Once the data sub_district vector is now stored inside the Sub_DistrictGroup vector, clear the sub_district vector in order to prepare it to receive
	   new set of sub-districts in the next province.
	7. Because the algorithm will store the sub_district vector inside the sub_districtGroup vector every time the <key> is "Province". If there is no
	   preceding "Province" then the last sub_district vector will not be added into the sub_districtGroup vector, thus it should be added once the
	   algorithm finishes parsing the input file.
	8. Because the algorithm will store the sub_district vector inside the sub_districtGroup vector every time the <key> is "Province". And given that "Province" will
	   appear before "Sub" (since the province has a higher hierarchy than the sub-district), this will make the first element of the sub_districtGroup vector
	   empty, which should be removed.
	*/

	while (inFile >> tempKey >> tempName >> tempLatitude >> tempLongitude >> tempPopulation >> tempArea) {  // 1
		// Disallow population and area value to be negative
		assert(tempPopulation >= 0);
		assert(tempArea >= 0);
		// 2
		if (tempKey.compare("Province") == 0) {  // 3
			province.push_back(Province(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
			sub_districtGroup.push_back(sub_district);  // 5
			sub_district.clear();  // 6
		}
		else if (tempKey.compare("Sub") == 0)  // 4
			sub_district.push_back(Sub_District(tempKey, tempName, tempLatitude, tempLongitude, tempPopulation, tempArea));
	}

	sub_districtGroup.push_back(sub_district);  // 7
	sub_districtGroup.erase(sub_districtGroup.begin());  // 8

	/** Compute and output statistics to a file **/
	/* Compare the population density in each provinces and sub_districts */
	ofstream outFile(OUTFILE);
	assert(outFile);  // Check whether output file is accessible or not

	outFile << "======================================================================" << endl;
	outFile << "[Summary Of Population Density In Each Provinces And Sub-Districts]\n" << endl;
	outFile << setprecision(9) << fixed;

	/* Output result to a file */
	for (unsigned int i = 0; i < province.size(); i++) {
		outFile << "Province " << province[i].getName() << setw(43 - province[i].getName().length()) << province[i].getPopulationDensity() << " people/sq.m." << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			outFile << "- " << sub_districtGroup[i][j].getName() << setw(50 - sub_districtGroup[i][j].getName().length()) << sub_districtGroup[i][j].getPopulationDensity() << " people/sq.m." << endl;
		outFile << endl;
	}

	/* Compare the sum of population in each provinces to the sum of population in sub_districts */
	outFile << "======================================================================" << endl;
	outFile << "[Summary Of Population In Each Provinces And Sub-Districts]\n" << endl;
	outFile << setprecision(0);

	for (unsigned int i = 0; i < province.size(); i++) {
		/* Get the difference between sum of each population in sub_districts */
		long long int sum_sub_district = 0;
		long long int difference;

		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++)
			sum_sub_district += sub_districtGroup[i][j].getPopulation();
		difference = province[i].getPopulation() - sum_sub_district;

		/* Output result to a file */
		outFile << "Province " << province[i].getName() << setw(49 - province[i].getName().length()) << province[i].getPopulation();
		(province[i].getPopulation() == 1) ? outFile << " person" << endl : outFile << " people" << endl;
		for (unsigned int j = 0; j < sub_districtGroup[i].size(); j++) {
			outFile << "- " << sub_districtGroup[i][j].getName() << setw(56 - sub_districtGroup[i][j].getName().length()) << sub_districtGroup[i][j].getPopulation();
			(sub_districtGroup[i][j].getPopulation() == 1) ? outFile << " person" << endl : outFile << " people" << endl;
		}

		/* If the population of the province does not match the sum of population in sub_districts, report extra population */
		if ((difference == 1) || (difference == -1))
			outFile << "Extra population from province: " << difference << " person" << endl;
		else if (difference != 0)
			outFile << "Extra population from province: " << difference << " people" << endl;
		outFile << endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}