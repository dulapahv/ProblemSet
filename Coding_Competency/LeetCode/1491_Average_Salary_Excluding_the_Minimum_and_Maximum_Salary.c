#include <stdio.h>

double average(int *salary, int salarySize)
{
    int max = salary[0];
    int min = salary[0];
    for (int i = 0; i < salarySize; i++)
    {
        if (salary[i] > max)
            max = salary[i];
        if (salary[i] < min)
            min = salary[i];
    }
    int sum = 0;
    int count = 0;
    for (int i = 0; i < salarySize; i++) {
        if (salary[i] != max && salary[i] != min) {
            sum += salary[i];
            count++;
        }
    }
    return sum / (count + 2);
}

int main()
{
    int salary[4] = {1000, 2000, 3000};
    printf("%lf", average(salary, 4));
}