/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_locate_obs.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tponutha <tponutha@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/29 12:08:37 by tponutha          #+#    #+#             */
/*   Updated: 2022/06/29 16:48:51 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

int	ft_obs_allocate(t_map *pmap)
{
	int	i;

	i = 0;
	pmap->obs_pos = malloc(sizeof(int *) * pmap->row);
	if (!pmap->obs_pos)
		return (1);
	while (i < pmap->row)
	{
		pmap->obs_pos[i] = (int *)malloc(sizeof(int) * pmap->col);
		if (!pmap->obs_pos[i])
		{
			i = 0;
			while (pmap->obs_pos[i])
			{
				free(pmap->obs_pos[i]);
				i++;
			}
			free(pmap->obs_pos);
			return (1);
		}
		i++;
	}
	return (0);
}

int	ft_fill_obs(t_map *pmap, char **box)
{
	int	i;
	int	j;

	i = 0;
	if (ft_obs_allocate(pmap))
		return (1);
	while (i < pmap->row)
	{
		j = 0;
		while (j < pmap->col)
		{
			if (pmap->obs == box[i][j])
				pmap->obs_pos[i][j] = 1;
			else
				pmap->obs_pos[i][j] = 0;
			j++;
		}
		i++;
	}
	return (0);
}
/*
#include <stdio.h>
int main()
{
	char *read = ft_readfile("../map1");
	char **b = ft_split(read, '\n');
	t_map map;
	map.row = 10;
	map.col = 10;
	map.obs = 'o';
	ft_locate_obs(&map, &b[1]);
	int i = 0;
	printf("-------------------------------\n");
	while (map.obs_pos[i])
	{
		printf("[%d,%d]\n",map.obs_pos[i][0],map.obs_pos[i][1]);
		i++;
	}
}
*/
