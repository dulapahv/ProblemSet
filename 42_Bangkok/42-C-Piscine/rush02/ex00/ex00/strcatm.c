/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strcatm.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: abossel <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/25 21:59:52 by abossel           #+#    #+#             */
/*   Updated: 2022/06/25 22:27:10 by abossel          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "strcatm.h"

int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len] != '\0')
		len++;
	return (len);
}

char	*strcatm(char *str1, char *str2)
{
	char	*str3;
	int		len1;
	int		len2;

	if (str1 == NULL || str2 == NULL)
		return (NULL);
	len1 = ft_strlen(str1);
	len2 = ft_strlen(str2);
	str3 = malloc(len1 + len2 + 1);
	if (str3 == NULL)
		return (NULL);
	len1 = 0;
	while (str1[len1] != '\0')
	{
		str3[len1] = str1[len1];
		len1++;
	}
	len2 = 0;
	while (str2[len2] != '\0')
	{
		str3[len1 + len2] = str2[len2];
		len2++;
	}
	str3[len1 + len2] = '\0';
	return (str3);
}
