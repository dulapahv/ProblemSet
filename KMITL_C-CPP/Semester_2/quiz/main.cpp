#include <iostream>

#include "Payroll.h"
#include "Fleet.h"

int main() {
    Bicycle bike1("Bicycles1", 500);
    Bicycle bike2("Bicycles2", 300);
    Jet jet1("Truck1", 4999, "PI3141");
    Jet jet2("Truck2", 5999, "TAO6283");
    Car car1("Car1", 4999, "LOL1234");
    Car car2("Car2", 5999, "SMH7894");

    Fleet fleet1 = Fleet();
    fleet1.addVehicle(&bike1);
    fleet1.addVehicle(&bike2);
    fleet1.addVehicle(&jet1);
    fleet1.addVehicle(&jet2);
    fleet1.addVehicle(&car1);
    fleet1.addVehicle(&car2);

    //fleet1.calcVehicleCost();


    TeaServer t1("John", 20, 5000);
    //cout << t1.calcSalary() << endl;
    SecurityGuard s1("Mary", 20, 8000);
    //cout << s1.calcSalary() << endl;
    Engineer e1("Tom", 20, 10000);
    //cout << e1.calcSalary() << endl;
    Mechanic m1("Jerry", 20, 8000, vector<Vehicle>{bike1, car1, jet1});
    //cout << m1.calcSalary() << endl;

    Payroll payroll1 = Payroll();
    payroll1.addEmployee(&t1);
    payroll1.addEmployee(&s1);
    payroll1.addEmployee(&e1);
    payroll1.addEmployee(&m1);

    payroll1.print();
    payroll1.calcTotalWages();
    
    return 0;
}
