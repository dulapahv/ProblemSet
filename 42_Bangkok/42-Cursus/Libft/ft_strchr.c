/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:50:53 by duvibuls          #+#    #+#             */
/*   Updated: 2022/08/10 20:50:53 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	char	*ptr;

	ptr = (char *)s;
	if (c >= 0 && c <= 127)
	{
		while (*ptr != c)
		{
			if (!*ptr)
				return (NULL);
			ptr++;
		}
		return (ptr);
	}
	return ((char *)s);
}
