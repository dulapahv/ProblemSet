/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:50:55 by duvibuls          #+#    #+#             */
/*   Updated: 2022/08/10 20:50:55 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	int		i;
	int		len1;
	int		len2;
	char	*dst;

	if (s1 && s2)
	{
		len1 = ft_strlen(s1);
		len2 = ft_strlen(s2);
		dst = malloc(sizeof(char) * (len1 + len2 + 1));
		if (!dst)
			return (NULL);
		i = -1;
		while (s1[++i])
			dst[i] = s1[i];
		i = -1;
		while (s2[++i])
			dst[len1++] = s2[i];
		dst[len1] = '\0';
		return (dst);
	}
	return (NULL);
}
