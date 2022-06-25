/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   numdict.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: abossel <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 19:59:35 by abossel           #+#    #+#             */
/*   Updated: 2022/06/25 13:23:30 by abossel          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "utility.h"
#include "numdict.h"

void	add_num(t_dict *d, int num, char *str)
{
	int	i;

	i = 0;
	while (i < d->len)
	{
		if (d->dict[i].number == num && d->dict[i].is_number)
		{
			free(d->dict[i].word);
			d->dict[i].word = ft_strdup(str);
			return ;
		}
		i++;
	}
	if (d->len == d->size)
		if (!extend_dict(d))
			return ;
	d->dict[i].number = num;
	d->dict[i].is_number = 1;
	d->dict[i].word = ft_strdup(str);
	d->len++;
}

void	add_mag(t_dict *d, int mag, char *str)
{
	int	i;

	i = 0;
	while (i < d->len)
	{
		if (d->dict[i].number == mag && !d->dict[i].is_number)
		{
			free(d->dict[i].word);
			d->dict[i].word = ft_strdup(str);
			return ;
		}
		i++;
	}
	if (d->len == d->size)
		if (!extend_dict(d))
			return ;
	d->dict[i].number = mag;
	d->dict[i].is_number = 0;
	d->dict[i].word = ft_strdup(str);
	d->len++;
}

char	*get_num_word(t_dict *d, int num)
{
	int	i;

	i = 0;
	while (i < d->len)
	{
		if (d->dict[i].number == num && d->dict[i].is_number)
			return (d->dict[i].word);
		i++;
	}
	return (NULL);
}

char	*get_mag_word(t_dict *d, int mag)
{
	int	i;

	i = 0;
	while (i < d->len)
	{
		if (d->dict[i].number == mag && !d->dict[i].is_number)
			return (d->dict[i].word);
		i++;
	}
	return (NULL);
}
