#include "headers.h"

int	ft_is_num(char c)
{
	if (c <= '9' && c >= '0')
		return (1);
	return (0);
}

/*
If the number of number in the argument is the size * 4 and number is less than size and number is not zero then valid.
*/
int	ft_check_count(int count, int size, int number)
{
	if (count == size * 4 && number <= size && number >= 1)
		return (0);
	return (1);
}

/*
1. Check whether the first character is number or not
2. If it is not a number, go to next character (but don't exit loop yet)
3. If it is not a number or higher than the size (i.e. 4x4 table but number is > 4) or it is a negative number, return 0 (error)
4. If the above condition checks out (number is valid), convert string to int (atoi()) and count how many numbers are in the string. Then return it to check

12 34
1. check if first character is a number or not. If it is, store in variable
var = 1
2. Check if the second character is a number or not. If it isn't, increase count by 1 (so we know that we can know how much number is in the argument)
3. Check if the second character is a number or not. If it is, multiply stored var by 10 and add current number
var = (1 * 10) + 2 = 12
*/ 

int	is_input_valid(char *str, int size, int *arr)
{
	int	n;
    int i;
	int	count;
	int	number;

	n = 0;
	number = 0;
	count = 0;
	if (ft_is_num(str[n]))
	{
		while (str[n])
		{
			if (!ft_is_num(str[n]))
				n++;
			if (!ft_is_num(str[n]) || size < number || number < 0)
				return (0);
			number = 0;
			while (ft_is_num(str[n]))
			{
				number = (number * 10) + str[n] - '0';
				if (!ft_is_num(str[++n]))
					count++;
			}
            arr[i] = number;
            i++;
		}
	}
	return (ft_check_count(count, size, number));
}