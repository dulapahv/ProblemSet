#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    int AMEXCheck = 0;
    int VISACheck = 0;
    int VISAVerify = 0;
    int MASTERCARDCheck = 0;
    long int Number;
    long int VISAoddcheck1, VISAoddcheck2, VISAoddcheck3, VISAoddcheck4, VISAoddcheck5, VISAoddcheck6, VISAoddcheck7, VISAoddcheck8;
    long int VISAevencheck1, VISAevencheck2, VISAevencheck3, VISAevencheck4, VISAevencheck5, VISAevencheck6, VISAevencheck7, VISAevencheck8;
    int VISAodd1=0, VISAodd2=0, VISAodd3=0, VISAodd4=0, VISAodd5=0, VISAodd6=0, VISAodd7=0, VISAodd8=0;
    int VISAeven1=0, VISAeven2=0, VISAeven3=0, VISAeven4=0, VISAeven5=0, VISAeven6=0, VISAeven7=0, VISAeven8=0;
    int VISAfinalOdd, VISAfinalEven;
    int VISAfinal;
    
    Number = get_long("Number: "); // Get number
    if (Number <= 1000000000000 || Number >= 9999999999999999) // Check whether input is not between 13-16 digits
    {
        printf("INVALID\n");
    }
    else
    {
        if (Number >= 100000000000000 && Number <= 999999999999999) // Check if 15 digits (AMEX and VISA)
        {
            AMEXCheck = floor (Number / 10000000000000); // Gets the first digit of Number and round down
            if (AMEXCheck == 34 || AMEXCheck == 37) // Check whether Number begins with 34/37
            {
                printf("AMEX\n");
            }
            else 
            {
                VISACheck = floor (Number / 100000000000000); // Gets the first digit of Number and round down
                if (VISACheck == 4)  // Gets the first digit of Number and round down
                {
                    printf("VISA\n");
                }
                else 
                {
                    printf("INVALID\n");
                }
            }
        }
    }
    if (Number <= 1000000000000 || Number >= 9999999999999999) // Check whether input is not between 13-16 digits
    {
        // leave empty
    }
    else {
        if (Number >= 1000000000000 && Number <= 9999999999999) // Check if Visa (13 Digits)
        {
            VISACheck = floor (Number / 1000000000000); // Gets the first digit of Number and round down
            if (VISACheck == 4) // Check whether Number Begins with 4
            {
                printf("VISA\n");
            }
            else 
            {
                printf("INVALID\n");
            }
        }
    }
    if (Number <= 1000000000000 || Number >= 9999999999999999) // Check whether input is not between 13-16 digits
    {
        // leave empty
    }
    else 
    {
        if (Number >= 10000000000000 && Number <= 99999999999999) // Check if Visa (14 Digits)
        {
            VISACheck = floor (Number / 10000000000000); // Gets the first digit of Number and round down
            if (VISACheck == 4)
            {
                printf("VISA\n");
            }
            else 
            {
                printf("INVALID\n");
            }
        }
    }
    if (Number <= 1000000000000 || Number >= 9999999999999999) // Check whether input is not between 13-16 digits
    {
        // leave empty
    }
    else 
    {
        if (Number >= 1000000000000000 && Number <= 9999999999999999) // Check if Visa (16 Digits)
        {
        // Dividing into odd/even digit place (123456 -> 1,123,12345)
        VISAoddcheck1 = Number/1000000000000000;
        VISAevencheck1 = Number/100000000000000;
        VISAoddcheck2 = Number/10000000000000;
        VISAevencheck2 = Number/1000000000000;
        VISAoddcheck3 = Number/100000000000;
        VISAevencheck3 = Number/10000000000;
        VISAoddcheck4 = Number/1000000000;
        VISAevencheck4 = Number/100000000;
        VISAoddcheck5 = Number/10000000;
        VISAevencheck5 = Number/1000000;
        VISAoddcheck6 = Number/100000;
        VISAevencheck6 = Number/10000;
        VISAoddcheck7 = Number/1000;
        VISAevencheck7 = Number/100;
        VISAoddcheck8 = Number/10;
        VISAevencheck8 = Number/1;
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
    else 
    {
        MASTERCARDCheck = floor (Number / 100000000000000); // Gets the first digit of Number and round down
        if (MASTERCARDCheck == 51 || MASTERCARDCheck == 52 || MASTERCARDCheck == 53 || MASTERCARDCheck == 54 || MASTERCARDCheck == 55) // Check whether Number begins with 51/52/53/54/55
    {
                printf ("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
        }
    }
}
