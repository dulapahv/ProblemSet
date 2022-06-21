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

#include "headers.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int error(void)
{
	ft_putstr("Error\n");
	return (0);
}

int main(int argc, char **argv)
{
	int size;
	int arr[16];
	// int	**table;

	// table = NULL;
	size = 4;
	if (argc != 2)
		return (error());
	if (is_input_valid(argv[1], size, arr))
		return (error());

	int grid[4][4] = {0};
	int top[4] = {arr[0], arr[1], arr[2], arr[3]};
	int bottom[4] = {arr[4], arr[5], arr[6], arr[7]};
	int left[4] = {arr[8], arr[9], arr[10], arr[11]};
	int right[4] = {arr[12], arr[13], arr[14], arr[15]};
	fill_4(grid, top, bottom, left, right);
	fill_1(grid, top, bottom, left, right);

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf("%d ", grid[i][j]);
		printf("\n");
	}
}
