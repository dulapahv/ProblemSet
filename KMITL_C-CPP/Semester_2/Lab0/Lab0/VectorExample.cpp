// Vector code examples
//

#include <iostream>
#include<iterator> // for iterators
#include<vector> // for vectors
using namespace std;

bool VectorExampleA() {
	cout << "Vector example" << endl;

	vector<int> ar = { 1, 2, 3, 4, 5 }; // Create an int vector
	size_t n = ar.size();
	cout << "Vector: " << n << " elements" << endl;
	for (size_t j = 0; j < n; j++) { cout << ar[j] << " "; }
	cout << endl;
	cout << "Add some elements" << endl;
	ar.push_back(101); ar.push_back(102);
	n = ar.size();
	cout << "Vector: " << n << " elements" << endl;
	for (size_t j = 0; j < n; j++) { cout << ar[j] << " "; }
	cout << endl;

	cout << "Print elements with iterator" << endl;
	vector<int>::iterator iter;
	for (iter = ar.begin(); iter != ar.end(); iter++) {
		cout << *iter << " ";
	}
	cout << endl;

	return true;
}

bool VectorExampleString() {
	cout << "Vector example" << endl;

	vector<string> sv = { "Leo", "Chang", "Singh" }; // Create an string vector
	size_t n = sv.size();
	cout << "Vector: " << n << " elements" << endl;
	for (size_t j = 0; j < n; j++) { cout << sv[j] << " "; }
	cout << endl;
	cout << "Add some elements" << endl;
	sv.push_back("Bintang"); sv.push_back("Ebisu");
	n = sv.size();
	cout << "Vector: " << n << " elements" << endl;
	for (size_t j = 0; j < n; j++) { cout << sv[j] << " "; }
	cout << endl;

	cout << "Print elements with iterator" << endl;
	vector<string>::iterator iter;
	for (iter = sv.begin(); iter != sv.end(); iter++) {
		cout << *iter << " ";
	}
	cout << endl;

	return true;
}
