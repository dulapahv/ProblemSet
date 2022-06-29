/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tponutha <tponutha@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 17:00:59 by tponutha          #+#    #+#             */
/*   Updated: 2022/06/29 16:50:54 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

void	ft_free_if(char ***box, int n)
{
	int	i;

	i = 0;
	while (i < n - 1)
	{
		free(box[0][i]);
		i++;
	}
	free(box[0]);
}

char	**ft_allocate(char **bigbox, char *str, char c)
{
	int	size;
	int	n;
	int	sptcount;

	n = 0;
	sptcount = ft_wordcount(str, c);
	bigbox = malloc(sizeof(char *) * (sptcount + 2));
	if (!bigbox)
		return (NULL);
	while (str[0])
	{
		size = ft_ptr_strlen(&str, '\n');
		bigbox[n] = (char *)malloc(sizeof(char) * size + 1);
		if (!bigbox[n])
		{
			ft_free_if(&bigbox, n);
			return (NULL);
		}
		if (str[0])
			str++;
		n++;
	}
	bigbox[n] = NULL;
	return (bigbox);
}

char	**ft_fill_word(char **bigbox, char *str, char spt)
{
	int	i;
	int	j;
	int	k;

	i = 0;
	j = 0;
	k = 0;
	while (str[i])
	{
		if (str[i] != spt)
		{
			bigbox[j][k] = str[i];
			k++;
		}
		else
		{
			k = 0;
			j++;
		}
		i++;
	}
	return (bigbox);
}

char	**ft_split(char *str, char spliter)
{
	char	**bigbox;

	bigbox = NULL;
	bigbox = ft_allocate(bigbox, str, spliter);
	if (!bigbox)
		return (NULL);
	bigbox = ft_fill_word(bigbox, str, spliter);
	return (bigbox);
}
/*
#include <stdio.h>
int main(int ac, char **av)
{
	if (ac != 2)
		return (0);
	char *b = ft_readfile(av[1]);
	char **a = ft_split(b, '\n');
	int i = 0;
	while (a[i] != NULL)
	{
		printf("%s\n",a[i]);
		i++;
	}
	return (0);
}
*/
