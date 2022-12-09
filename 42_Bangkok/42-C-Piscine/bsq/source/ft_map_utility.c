/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_map_utility.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 02:32:34 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/29 16:49:36 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

void	ft_setup_object(t_map *pmap, char **box)
{
	int	firstlen;

	firstlen = ft_strlen(box[0]);
	pmap->square = box[0][firstlen - 1];
	pmap->obs = box[0][firstlen - 2];
	pmap->free = box[0][firstlen - 3];
	if (firstlen == 4)
		pmap->row = box[0][0] - '0';
	else if (firstlen == 5)
		pmap->row = (box[0][0] - '0') * 10 + (box[0][1] - '0');
	pmap->col = ft_strlen(box[1]);
}

int	ft_map_allocate(t_map *pmap)
{
	int	i;

	i = 0;
	pmap->arr = malloc(sizeof(int *) * pmap->row);
	if (!pmap->arr)
		return (1);
	while (i < pmap->row)
	{
		pmap->arr[i] = (int *)malloc(sizeof(int) * pmap->col);
		if (!pmap->arr[i])
		{
			i = 0;
			while (pmap->arr[i])
			{
				free(pmap->arr[i]);
				i++;
			}
			free(pmap->arr);
			return (1);
		}
		i++;
	}
	return (0);
}

int	ft_fill_arr(t_map *pmap)
{
	int	i;
	int	j;
	int	flag;

	i = 0;
	flag = ft_map_allocate(pmap);
	if (flag)
		return (1);
	while (i < pmap->row)
	{
		j = 0;
		while (j < pmap->col)
		{
			pmap->arr[i][j] = 0;
			j++;
		}
		i++;
	}
	return (0);
}

void	*ft_free_if_fail(t_map **pmap, char ***box, int round)
{
	if (round >= 1)
		ft_free_box(box);
	if (round >= 2)
		ft_free_arr(pmap[0]);
	free(pmap[0]);
	return (NULL);
}

t_map	*ft_create_map(char *content)
{
	char	**box;
	t_map	*pmap;

	if (!content)
		return (NULL);
	pmap = (t_map *)malloc(sizeof(t_map));
	if (!pmap)
		return (NULL);
	box = ft_split(content, '\n');
	if (!box)
		return (ft_free_if_fail(&pmap, &box, 0));
	ft_setup_object(pmap, box);
	if (ft_fill_arr(pmap))
		return (ft_free_if_fail(&pmap, &box, 1));
	if (ft_fill_obs(pmap, &box[1]))
		return (ft_free_if_fail(&pmap, &box, 2));
	ft_free_box(&box);
	return (pmap);
}
