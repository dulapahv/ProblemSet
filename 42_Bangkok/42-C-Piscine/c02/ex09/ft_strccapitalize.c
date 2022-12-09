/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strccapitalize.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/12 12:13:25 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/12 13:48:40 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if ((i == 0) && ((str[i] >= 'a') && (str[i] <= 'z')))
			str[i] -= 32;
		if ((i > 0) && ((str[i] >= 'a') && (str[i] <= 'z')))
		{
			if (!((str[i - 1] >= '0') && (str[i - 1] <= '9')))
			{
				if ((str[i - 1] < 'A') || (str[i - 1] > 'Z'))
				{
					if ((str[i - 1] < 'a') || (str[i - 1] > 'z'))
						str[i] -= 32;
				}
				else if ((str[i - 1] < 'a') || (str[i - 1] > 'z'))
					if ((str[i - 1] < 'A') || (str[i - 1] > 'Z'))
						str[i] -= 32;
			}
		}
		i++;
	}
	return (str);
}
