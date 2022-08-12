/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:51:02 by duvibuls          #+#    #+#             */
/*   Updated: 2022/08/10 20:51:02 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	char	*ptr;

	ptr = NULL;
	if (c >= 0 && c <= 127)
	{
		while (*s)
		{
			if (*s == c)
				ptr = (char *)s;
			s++;
		}
		if (!c)
			return ((char *)s);
		return (ptr);
	}
	return ((char *)s);
}
