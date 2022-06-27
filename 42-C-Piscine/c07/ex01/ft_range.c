/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 14:03:43 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/24 14:09:48 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	range;
	int	i;
	int	*arr;

	if (min >= max)
		return (0);
	range = max - min - 1;
	arr = malloc(range * sizeof(int));
	if (!arr)
		return (0);
	i = 0;
	while (i <= range)
	{
		arr[i] = min + i;
		i++;
	}
	return (arr);
}
