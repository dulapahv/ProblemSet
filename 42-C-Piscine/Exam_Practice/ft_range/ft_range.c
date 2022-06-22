/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/22 19:29:58 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/22 19:57:35 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	ft_swap(int *a, int *b)
{
	int	c;

	c = *a;
	*a = *b;
	*b = c;
}

int	*ft_range(int start, int end)
{
	int	inversed;
	int	range;
	int	*arr;
	int	i;

	if (start > end)
		inversed = 1;
	else
		inversed = 0;
	if (inversed)
		ft_swap(&start, &end);
	range = end - start + 1;
	arr = (int *)malloc((range + 2) * sizeof(int));
	if (!arr)
		return (NULL);
	i = 0;
	while (i < range)
	{
		if (inversed)
			arr[range - 1 - i] = start + i;
		else
			arr[i] = start + i;
		i++;
	}
	return (arr);
}
