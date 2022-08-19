/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/08/10 20:50:51 by duvibuls          #+#    #+#             */
/*   Updated: 2022/08/10 20:50:51 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	**ft_split(char const *s, char c)
{
	char	**result;
	int		set;
	int		len;
	int		i;
	int		j;

	set = 0;
	len = 0;
	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			set++;
		i++;
	}
	result = malloc(sizeof(char *) * set);
	if (!result)
		return (NULL);
	i = 0;
	set = 0;
	while (s[i])
	{
		if (s[i] != c)
			len++;
		else
		{
			result[set] = malloc(sizeof(char) * (len + 1));
			if (!result[set])
				return (NULL);
			set++;
			len = 0;
		}
		i++;
	}
	i = 0;
	set = 0;
	j = 0;
	while (s[i])
	{
		if (s[i] != c)
		{
			result[set][j] = s[i];
			j++;
		}
		else
		{
			result[set][j] = '\0';
			set++;
			j = 0;
		}
		i++;
	}
	return (result);
}
