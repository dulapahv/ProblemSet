/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/18 14:20:40 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/18 14:20:45 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// #include "fill_4.c"
// #include "fill_1.c"

#include "headers.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// int ft_strlen(char *str)
// {
// 	int i;

// 	i = 0;
// 	while (str[i] != '\0')
// 		i++;
// 	return (i);
// }

// int ft_is_space(char c)
// {
//     if (c == ' ' || c == '\t' || c == '\n' || c == '\v' || c == '\f' || c == '\r')
//         return (1);
//     else
//         return (0);
// }

// int ft_negative(char c)
// {
//     if (c == '-')
//         return (-1);
//     if (c == '+')
//         return (1);
//     else
//         return (0);
// }

// int ft_atoi(char *str)
// {
//     int minus;
//     int result;

//     result = 0;
//     minus = 1;
//     while (ft_is_space(*str))
//         str++;
//     while (ft_negative(*str) == -1 || ft_negative(*str) == 1)
//     {
//         minus *= ft_negative(*str);
//         str++;
//     }
//     while (*str != '\0')
//     {
//         if (*str >= '0' && *str <= '9')
//         {
//             result *= 10;
//             result += ((int)(*str - '0'));
//         }
//         else
//             break;
//         str++;
//     }
//     return (result * minus);
// }

// void parse_input(char *arr, int *top, int bottom[4], int left[4], int right[4])
// {
//     char buf[] = "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2";
//     int nums[128], n = 0;

//     char *p = buf;
//     while (*p)
//     {
//         while (*p && (*p == ' ' || *p == '\t' || *p == '\n'))
//             p++;

//         if (*p)
//         {
//             nums[n++] = ft_atoi(p);
//             while (*p && *p != ' ' && *p != '\t' && *p != '\n')
//                 p++;
//         }
//     }
// }

// void create_grid(int **grid)
// {
// 	int i;
// 	grid = (int**) malloc(4 * sizeof(int*));
//    	for (i = 0; i < 4; i++)
//        grid[i] = (int*) calloc(4, sizeof(int));
// }



int	error(void)
{
	ft_putstr("Error\n");
	return (0);
}

int	main(int argc, char **argv)
{
	int	size;
	int arr[16];
	// int	**table;

	// table = NULL;
	size = 4;
	if (argc != 2)
		return(error());
	if (is_input_valid(argv[1], size, arr))
		return(error());

	//malloc array of 4 integers
	//int *top = (int*) malloc(sizeof(int) * 4);
	int grid[4][4] = {0};
	int top[4] = {arr[0],arr[1],arr[2],arr[3]};
	int bottom[4] = {arr[4],arr[5],arr[6],arr[7]};
	int left[4] = {arr[8],arr[9],arr[10],arr[11]};
	int right[4] = {arr[12],arr[13],arr[14],arr[15]};
	fill_4(grid, top, bottom, left, right);
	fill_1(grid, top, bottom, left, right);

	// printf("top: %d %d %d %d\n", top[0], top[1], top[2], top[3]);
	// printf("bottom: %d %d %d %d\n", bottom[0], bottom[1], bottom[2], bottom[3]);
	// printf("left: %d %d %d %d\n", left[0], left[1], left[2], left[3]);
	// printf("right: %d %d %d %d\n", right[0], right[1], right[2], right[3]);

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf("%d ", grid[i][j]);
		printf("\n");
	}
	// for (int i = 0; i < 16; i++)
	// 	printf("%d ", arr[i]);
	//table = ft_init(size, argv[1]);
}

// int main(int argc, char **argv)
// {
// 	// int top[4] = {4, 3, 2, 1};
// 	// int bottom[4] = {1, 2, 2, 2};
// 	// int left[4] = {4, 3, 2, 1};
// 	// int right[4] = {1, 2, 2, 2};
// 	int top[4] = {1, 2, 3, 3};
// 	int bottom[4] = {3, 3, 1, 2};
// 	int left[4] = {1, 2, 2, 2};
// 	int right[4] = {4, 3, 1, 2};
// 	// int top[4];
// 	// int bottom[4];
// 	// int left[4];
// 	// int right[4];
// 	//int **grid;
// 	int grid[4][4] = {0};
// 	//parse_input(arg, top, bottom, left, right);

// 	//create_grid(grid);




// 	// for (int i = 0; i < 4; i++)
// 	// 	free(grid[i]);
// }

// // "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2"

// ./rush-01 "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2" | cat -e

	
	//
	// int top[4] = {0};
	// int bottom[4] = {0};
	// int left[4] = {0};
	// int right[4] = {0};

	// int i;
	// int j;
	// while (i < 4)
	// {
	// 	top[i] = arr[j++];
	// 	i++;
	// }
	// i = 0;
	// while (i < 4)
	// {
	// 	bottom[i] = arr[j++];
	// 	i++;
	// }
	// i = 0;
	// while (i < 4)
	// {
	// 	left[i] = arr[j++];
	// 	i++;
	// }
	// i = 0;
	// while (i < 4)
	// {
	// 	right[i] = arr[j++];
	// 	i++;
	// }