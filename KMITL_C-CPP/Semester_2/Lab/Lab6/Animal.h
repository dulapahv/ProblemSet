// Multiple Inheritance Example

#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>

#include "Monkey.h"

#include "DivideByZeroException.h"
#include "OverflowException.h"



int main()
{
    Monkey m1;
    m1.printM();
    Monkey m2("Grey Monkey");
    fprintf(stdout, "%s skeleton is %10.2f m long\n", m2.getCommonName().c_str(), m2.getLength());
}