/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_god_of_free.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tponutha <tponutha@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/29 13:40:37 by tponutha          #+#    #+#             */
/*   Updated: 2022/06/29 16:48:19 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

void	ft_free_box(char ***box)
{
	int	i;

	i = 0;
	while (box[0][i])
	{
		free(box[0][i]);
		i++;
	}
	free(box[0]);
}

void	ft_free_arr(t_map *map)
{
	int	i;

	i = 0;
	while (i < map->row)
	{
		free(map->arr[i]);
		i++;
	}
	free(map->arr);
}

void	ft_free_complete_map(t_map **map)
{
	int	i;

	i = 0;
	free(map[0]->ans_pos_start);
	free(map[0]->ans_pos_end);
	ft_free_arr(map[0]);
	while (map[0]->obs_pos[i])
	{
		free(map[0]->obs_pos[i]);
		i++;
	}
	free(map[0]->obs_pos);
	free(map[0]);
}
