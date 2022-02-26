// ExampleA.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "Rectangle.h"
#include "Complex.h"
#include "Point.h"
#include <chrono>
#include <vector> // for vectors

const int n_max = 10000;

int main() {
	std::vector<Rectangle> vr;
	Point p1, p2;
	p1 = Point(1.0, 1.0);
	p2 = Point(2.0, 4.0);
	Rectangle ra(p1, p2);

	std::cout << "Make a vector " << std::endl;

	size_t n_current = vr.size();
	size_t n_cap = vr.capacity();
	size_t max_size = 0;
	std::cout << "Init elem " << n_current << " cap " << n_cap << std::endl;

	std::chrono::steady_clock::time_point t1 = std::chrono::steady_clock::now();

	for (int j = 0; j < n_max; j++) {
		// Add some code here to show us how vector allocates space on YOUR computer
		vr.push_back(ra);
		std::cout << "Added 1 element. Size: " << vr.size() << " | Capacity: " << vr.capacity() << std::endl;
	}

	std::chrono::steady_clock::time_point t2 = std::chrono::steady_clock::now();
	std::chrono::duration<double> time_first = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);

	// Print some conclusions here .. how many extra elements are added
	// whenever the vector becomes full
	int size1 = vr.size();
	int capacity1 = vr.capacity();
	std::cout << "\nCONCLUSION - Inserting " << n_max << " elements WITHOUT reserve" << std::endl;
	std::cout << "Size of vector: " << size1 << std::endl;
	std::cout << "Capacity of vector: " << capacity1 << std::endl;
	std::cout << "Time: " << time_first.count() * 1000 << " milliseconds." << std::endl;
	system("pause");

	// Try using reserve here to see what happens?  Can you adjust the
	// extra space allocated ??
	vr.clear();
	vr.shrink_to_fit();
	vr.reserve(n_max);

	std::chrono::steady_clock::time_point t3 = std::chrono::steady_clock::now();

	for (int j = 0; j < n_max; j++) {
		// Now show us how vector allocates space on YOUR computer after reserve
		vr.push_back(ra);
		std::cout << "Added 1 element. Size: " << vr.size() << " | Capacity: " << vr.capacity() << std::endl;
	}

	std::chrono::steady_clock::time_point t4 = std::chrono::steady_clock::now();
	std::chrono::duration<double> time_second = std::chrono::duration_cast<std::chrono::duration<double>>(t4 - t3);

	int size2 = vr.size();
	int capacity2 = vr.capacity();
	std::cout << "\nCONCLUSION - Inserting " << n_max << " elements WITH reserve" << std::endl;
	std::cout << "Size of vector: " << size2 << std::endl;
	std::cout << "Capacity of vector: " << capacity2 << std::endl;
	std::cout << "Time: " << time_second.count() * 1000 << " milliseconds" << std::endl;

	std::cout << "\n==================================================" << std::endl;
	std::cout << "[SUMMARY]" << std::endl;
	std::cout << "\nInserting " << n_max << " elements WITHOUT reserve" << std::endl;
	std::cout << "Size of vector: " << size1 << std::endl;
	std::cout << "Capacity of vector: " << capacity1 << std::endl;
	std::cout << "Time: " << time_first.count() * 1000 << " milliseconds." << std::endl;

	std::cout << "\nInserting " << n_max << " elements WITH reserve" << std::endl;
	std::cout << "Size of vector: " << size2 << std::endl;
	std::cout << "Capacity of vector: " << capacity2 << std::endl;
	std::cout << "Time: " << time_second.count() * 1000 << " milliseconds" << std::endl;

	std::cout << "\n- Without using reserve(), if you push_back another element into a full vector, "
		"then it will typically allocate double (or 1.5 * current size) the memory it's currently using" << std::endl;
	std::cout << "- With reserve(), it allows you to pre-allocate memory for the vector if you know its certain size, "
		"and avoid reallocating memory every time space runs out." << std::endl;
	std::cout << "- This has an effect on execution time. You can see that filling elements into a reserved vector is faster "
		"since it does not have to reallocate more memory every time the vector is full." << std::endl;

	/*
	Without using reserve(), if you push_back another element into a full vector,
	then it will typically allocate double (or 1.5 * current size) the memory it's currently using

	With reserve(), it allows you to pre-allocate memory for the vector if you know its certain size,
	and avoid reallocating memory every time space runs out.

	This has an effect on execution time. You can see that filling elements into a reserved vector is faster
	since it does not have to reallocate more memory every time the vector is full.
	*/

	system("pause");
}