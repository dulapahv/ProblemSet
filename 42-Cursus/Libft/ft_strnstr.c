/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:51:01 by duvibuls          #+#    #+#             */
/*   Updated: 2022/08/10 20:51:01 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	char	*haystack_ptr;
	char	*needle_ptr;
	char	*start;
	int		flag;

	if (!needle)
		return ((char *)haystack);
	i = 0;
	haystack_ptr = (char *)haystack;
	needle_ptr = (char *)needle;
	flag = 0;
	while (*haystack_ptr && i < len)
	{
		if (*haystack_ptr == *needle_ptr)
		{
			if (flag == 0)
			{
				start = (char *)haystack_ptr;
				flag = 1;
			}
			needle_ptr++;
			if (!*needle_ptr)
				return (start);
		}
		else
		{
			needle_ptr = (char *)needle;
			flag = 0;
		}
		haystack_ptr++;
		i++;
	}
	return (NULL);
}
