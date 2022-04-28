#include <iostream>

#include "Vehicle.h"

using namespace std;


void Jet::print() {
    cout << "Jet: " << name << " Load : " << load_capacity << " Passenger : " << max_passenger << endl;
}


void Car::print() {
    cout << "Car: " << name << " Load : " << load_capacity << " Passenger : " << max_passenger << endl;
}


void Bicycle::print() {
    cout << "Bicycle: " << name << " Seats: " << seats << " Basket: " << hasBasket << endl;
}