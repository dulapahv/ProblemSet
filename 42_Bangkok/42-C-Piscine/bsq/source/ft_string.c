/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_string.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tponutha <tponutha@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 17:01:10 by tponutha          #+#    #+#             */
/*   Updated: 2022/06/28 17:01:11 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

int	ft_wordcount(char *str, char c)
{
	int	count;

	count = 0;
	while (str[0])
	{
		if (str[0] == c)
			count++;
		str++;
	}
	return (count);
}

int	ft_nptr_strlen(char *str, char c)
{
	int	len;

	len = 0;
	while (str[len] != c && str[len] != 0)
		len++;
	return (len);
}

int	ft_ptr_strlen(char **str, char c)
{
	int	len;

	len = 0;
	while (str[0][0] != c && str[0][0] != 0)
	{
		str[0]++;
		len++;
	}
	return (len);
}

int	ft_is_not_printable(char *str, char not)
{
	while (str[0])
	{
		if ((str[0] < 32 || str[0] == 127) && str[0] != not)
			return (1);
		str++;
	}
	return (0);
}

int	ft_is_same(char *str)
{
	int	i;
	int	j;
	int	len;

	i = 0;
	len = ft_nptr_strlen(str, '\n');
	while (i < len - 1)
	{
		j = i + 1;
		while (j < len)
		{
			if (str[j] == str[i])
				return (1);
			j++;
		}
		i++;
	}
	return (0);
}
/*
#include <stdio.h>
int  main()
{
	printf("%d\n",ft_is_same("asdfghjkla"));
}
*/