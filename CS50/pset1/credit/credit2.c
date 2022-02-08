#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <stdint.h>

int main(void)
{
    long int VISA;
    long int VISAoddcheck1, VISAoddcheck2, VISAoddcheck3, VISAoddcheck4, VISAoddcheck5, VISAoddcheck6, VISAoddcheck7, VISAoddcheck8;
    long int VISAevencheck1, VISAevencheck2, VISAevencheck3, VISAevencheck4, VISAevencheck5, VISAevencheck6, VISAevencheck7, VISAevencheck8;
    int VISAodd1=0, VISAodd2=0, VISAodd3=0, VISAodd4=0, VISAodd5=0, VISAodd6=0, VISAodd7=0, VISAodd8=0;
    int VISAeven1=0, VISAeven2=0, VISAeven3=0, VISAeven4=0, VISAeven5=0, VISAeven6=0, VISAeven7=0, VISAeven8=0;
    int VISAfinalOdd, VISAfinalEven;
    int VISAfinal;

    VISA = get_long("Number: "); // Get user input
    // Dividing into odd/even digit place (123456 -> 1,123,12345)
    VISAoddcheck1 = VISA/1000000000000000;
    VISAevencheck1 = VISA/100000000000000;
    VISAoddcheck2 = VISA/10000000000000;
    VISAevencheck2 = VISA/1000000000000;
    VISAoddcheck3 = VISA/100000000000;
    VISAevencheck3 = VISA/10000000000;
    VISAoddcheck4 = VISA/1000000000;
    VISAevencheck4 = VISA/100000000;
    VISAoddcheck5 = VISA/10000000;
    VISAevencheck5 = VISA/1000000;
    VISAoddcheck6 = VISA/100000;
    VISAevencheck6 = VISA/10000;
    VISAoddcheck7 = VISA/1000;
    VISAevencheck7 = VISA/100;
    VISAoddcheck8 = VISA/10;
    VISAevencheck8 = VISA/1;
    // Getting the last digit of the odd/even (1,123,12345 -> 1, 3, 5) and multiply each of them by 2 (only for odd)
    VISAodd1 = (2*(VISAoddcheck1%10));
    VISAodd2 = (2*(VISAoddcheck2%10));
    VISAodd3 = (2*(VISAoddcheck3%10));
    VISAodd4 = (2*(VISAoddcheck4%10));
    VISAodd5 = (2*(VISAoddcheck5%10));
    VISAodd6 = (2*(VISAoddcheck6%10));
    VISAodd7 = (2*(VISAoddcheck7%10));
    VISAodd8 = (2*(VISAoddcheck8%10));
    VISAeven1 = VISAevencheck1%10;
    VISAeven2 = VISAevencheck2%10;
    VISAeven3 = VISAevencheck3%10;
    VISAeven4 = VISAevencheck4%10;
    VISAeven5 = VISAevencheck5%10;
    VISAeven6 = VISAevencheck6%10;
    VISAeven7 = VISAevencheck7%10;
    VISAeven8 = VISAevencheck8%10;
    // If the odd result is >= 10 then convert to 2 digits then add up (12 -> 1 + 2)
    if (VISAodd1 >=10)
    {
        VISAodd1 = (VISAodd1%10)+(VISAodd1/10);
    }
    if (VISAodd2 >=10)
    {
        VISAodd2 = (VISAodd2%10)+(VISAodd2/10);
    }
    if (VISAodd3 >=10)
    {
        VISAodd3 = (VISAodd3%10)+(VISAodd3/10);
    }
    if (VISAodd4 >=10)
    {
        VISAodd4 = (VISAodd4%10)+(VISAodd4/10);
    }
    if (VISAodd5 >=10)
    {
        VISAodd5 = (VISAodd5%10)+(VISAodd5/10);
    }
    if (VISAodd6 >=10)
    {
        VISAodd6 = (VISAodd6%10)+(VISAodd6/10);
    }
    if (VISAodd7 >=10)
    {
        VISAodd7 = (VISAodd7%10)+(VISAodd7/10);
    }
    if (VISAodd8 >=10)
    {
        VISAodd8 = (VISAodd8%10)+(VISAodd8/10);
    }

    // Add all the odd/even result together
    VISAfinalOdd = VISAodd1+VISAodd2+VISAodd3+VISAodd4+VISAodd5+VISAodd6+VISAodd7+VISAodd8;
    VISAfinalEven = VISAeven1+VISAeven2+VISAeven3+VISAeven4+VISAeven5+VISAeven6+VISAeven7+VISAeven8;
    // Add all final result and get only the last digit
    VISAfinal = (VISAfinalOdd + VISAfinalEven)%10;
    // Check whether last digit = 0 or not
    if (VISAfinal==0)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}