#include <iostream>

using namespace std;

int main()
{
    std::array result[];
    for (int i = 1; i < 10; i++)
    {
        result[i] += result[i-1] + result[i-2];
        printf("%i\n", result[i]);
    }
    
}