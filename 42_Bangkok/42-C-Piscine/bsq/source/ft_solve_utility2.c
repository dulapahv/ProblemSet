/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_solve_utility2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 02:32:34 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/28 02:32:35 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

int	swarm_row(t_map *map)
{
	int	i;
	int	j;
	int	limit;

	i = map->ans_pos_start[1];
	limit = map->row;
	while (i < map->col)
	{
		j = map->ans_pos_start[0];
		while (j < limit)
		{
			if (map->obs_pos[j][i])
				limit = i;
			j++;
		}
		i++;
	}
	map->ans_pos_end[0] = limit + map->ans_pos_start[0];
	return (0);
}

int	swarm_col(t_map *map)
{
	int	i;
	int	j;
	int	limit;

	i = map->ans_pos_start[0];
	limit = map->col;
	while (i < map->row)
	{
		j = map->ans_pos_start[1];
		while (j < limit)
		{
			if (map->obs_pos[i][j])
				limit = j;
			j++;
		}
		i++;
	}
	map->ans_pos_end[1] = limit + map->ans_pos_start[1];
	return (0);
}

void	adjust(t_map *map)
{
	int	max;
	int	diff;

	if (map->ans_pos_end[0] > map->ans_pos_end[1])
		max = map->ans_pos_end[0];
	else
		max = map->ans_pos_end[1];
	if (max > map->row || max > map->col)
	{
		if (max - map->row > max - map->col)
			diff = max - map->row;
		else
			diff = max - map->col;
	}
	map->ans_pos_end[0] -= diff;
	map->ans_pos_end[1] -= diff;
}

void	adjust2(t_map *map)
{
	map->ans_pos_end[0] -= 1;
	map->ans_pos_end[1] -= 1;
}

void	ft_arr_print(t_map *map)
{
	int	i;
	int	j;

	i = 0;
	while (i < map->row)
	{
		j = 0;
		while (j < map->col)
		{
			if (i >= map->ans_pos_start[0] && i <= map->ans_pos_end[0]
				&& j >= map->ans_pos_start[1] && j <= map->ans_pos_end[1])
				write(1, &map->square, 1);
			else if (map->obs_pos[i][j])
				write(1, &map->obs, 1);
			else
				write(1, &map->free, 1);
			j++;
		}
		write(1, "\n", 1);
		i++;
	}
}
