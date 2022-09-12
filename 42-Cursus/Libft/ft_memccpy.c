/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:50:41 by duvibuls          #+#    #+#             */
/*   Updated: 2022/09/07 13:25:30 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memccpy(void *dst, const void *src, int c, size_t n)
{
	size_t			i;
	unsigned char	*source;
	unsigned char	*desti;

	i = 0;
	source = (unsigned char *)src;
	desti = (unsigned char *)dst;
	while (i < n)
	{
		desti[i] = source[i];

		i++;
	}
	return (NULL);
}
