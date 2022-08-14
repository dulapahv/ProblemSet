/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:51:04 by duvibuls          #+#    #+#             */
/*   Updated: 2022/08/10 20:51:04 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*ptr;
	size_t	i;
	char	*arr;

	ptr = (char *)s + start;
	i = 0;
	arr = malloc(sizeof(char) * (len + 1));
	if (!arr)
		return (NULL);
	while (*ptr && i < len)
	{
		*arr = *ptr;
		arr++;
		ptr++;
		i++;
	}
	*arr = '\0';
	return (arr);
}
