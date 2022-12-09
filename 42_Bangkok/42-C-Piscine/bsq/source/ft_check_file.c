/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_check_file.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tponutha <tponutha@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 17:00:17 by tponutha          #+#    #+#             */
/*   Updated: 2022/06/29 16:47:11 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"
#include <stdio.h>

int	ft_check_word(char *str, char free, char obs)
{
	while (str[0])
	{
		if (str[0] != free && str[0] != obs && str[0] != '\n')
			return (1);
		str++;
	}
	return (0);
}

int	ft_read_description(char *content)
{
	int	totalen;
	int	index;

	totalen = ft_nptr_strlen(content, '\n');
	if (totalen > 5 || totalen < 4)
		return (1);
	if (content[0] < '0' || content[0] > '9')
		return (1);
	if (totalen == 4)
		index = 1;
	else if (totalen == 5)
	{
		index = 2;
		if (content[1] < '0' || content[1] > '9')
			return (1);
	}
	if (ft_is_same(&content[index]))
		return (1);
	return (0);
}

int	ft_check_size(char *exclude_first, int row)
{
	int	column;
	int	tmpcolumn;

	if (ft_wordcount(exclude_first, '\n') + 1 != row)
		return (1);
	column = ft_ptr_strlen(&exclude_first, '\n');
	while (exclude_first[0])
	{
		if (exclude_first[0])
			exclude_first++;
		tmpcolumn = ft_ptr_strlen(&exclude_first, '\n');
		if (tmpcolumn != column)
			return (1);
	}
	return (0);
}

int	ft_check_file(char *content)
{
	int		row;
	int		firstlen;
	char	free;
	char	obstacle;

	if (ft_is_not_printable(content, '\n'))
		return (1);
	if (ft_read_description(content))
		return (1);
	firstlen = ft_nptr_strlen(content, '\n');
	row = content[0] - '0';
	if (firstlen == 5)
		row = row * 10 + (content[1] - '0');
	free = content[firstlen - 3];
	obstacle = content[firstlen - 2];
	if (ft_check_size(&content[firstlen + 1], row))
		return (1);
	if (ft_check_word(&content[firstlen + 1], free, obstacle))
		return (1);
	return (0);
}

/*
int main()
{
	char *a = ft_readfile("../map/map1");
	printf("%d\n",ft_check_file(a));
}
*/
