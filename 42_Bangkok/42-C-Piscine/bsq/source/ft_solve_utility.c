/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_solve_utility.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 02:32:34 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/28 02:32:35 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

void	reverse(t_map *map)
{
	int	i;
	int	j;

	i = 0;
	while (i < map->row)
	{
		j = 0;
		while (j < map->col)
		{
			if (i == map->row - 1 && map->arr[i][j] == 0)
				map->arr[i][j] = 1;
			if (j == map->col - 1 && map->arr[i][j] == 0)
				map->arr[i][j] = 1;
			if (map->arr[i][j] == map->obs_pos[i][j])
				map->arr[i][j] = 0;
			j++;
		}
		i++;
	}
}

int	min3(int a, int b, int c)
{
	int	min;

	min = a;
	if (b < min)
		min = b;
	if (c < min)
		min = c;
	return (min);
}

void	back_traverse(t_map *map)
{
	int	i;
	int	j;

	i = map->row - 1;
	while (i >= 0)
	{
		j = map->col - 1;
		while (j >= 0)
		{
			if (!map->obs_pos[i][j])
				if (i <= map->row - 2 && j <= map->col - 2)
					map->arr[i][j] = 1 + min3(map->arr[i][j + 1],
							map->arr[i + 1][j + 1], map->arr[i + 1][j]);
			j--;
		}
		i--;
	}
}

void	find_max(t_map *map)
{
	int	i;
	int	j;

	map->max = map->arr[0][0];
	i = 0;
	while (i < map->row)
	{
		j = 0;
		while (j < map->col)
		{
			if (map->arr[i][j] > map->max)
				map->max = map->arr[i][j];
			j++;
		}
		i++;
	}
}

int	find_ans_pos(t_map *map)
{
	int	i;
	int	j;

	i = 0;
	map->ans_pos_start = (int *)malloc(2 * sizeof(int));
	map->ans_pos_end = (int *)malloc(2 * sizeof(int));
	while (i < map->row)
	{
		j = 0;
		while (j < map->col)
		{
			if (map->arr[i][j] == map->max)
			{
				map->ans_pos_start[0] = i;
				map->ans_pos_start[1] = j;
				return (0);
			}
			j++;
		}
		i++;
	}
	return (0);
}
