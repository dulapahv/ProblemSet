#include <iostream>

using namespace std;

int main() {
	int a = INT_MAX;  // a = 2147483647

	if (a + 10000 > INT_MAX) {  // This will surely make 'a' greater than the integer limit
		cout << "Overflow!" << endl;
	}
	else {
		cout << "No Overflow!" << endl;
	}

	cout << "a is " << a << endl;  
	// However, 'a' becomes 2147483647 which makes checking in line 8 unable to check overflow and causes undefined behavior.
}