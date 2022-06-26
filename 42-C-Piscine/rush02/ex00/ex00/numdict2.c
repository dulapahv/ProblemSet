/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   numdict2.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: abossel <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 19:59:35 by abossel           #+#    #+#             */
/*   Updated: 2022/06/25 20:37:50 by abossel          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

#include "numdict.h"
#include "ft_put.h"

int	create_dict(t_dict *d)
{
	d->dict = malloc(sizeof(t_dict_elem) * DICT_SIZE);
	d->size = DICT_SIZE;
	d->len = 0;
	if (d->dict == NULL)
		return (0);
	return (1);
}

int	extend_dict(t_dict *d)
{
	t_dict_elem	*t;
	int			i;

	t = malloc(sizeof(t_dict_elem) * (d->size + DICT_SIZE));
	if (t == NULL)
		return (0);
	i = 0;
	while (i < d->len)
	{
		t[i].number = d->dict[i].number;
		t[i].is_number = d->dict[i].is_number;
		t[i].word = d->dict[i].word;
		i++;
	}
	free(d->dict);
	d->dict = t;
	d->size += DICT_SIZE;
	return (1);
}

void	free_dict(t_dict *d)
{
	int	i;

	if (d->dict == NULL)
		return ;
	i = 0;
	while (i < d->len)
	{
		free(d->dict[i].word);
		i++;
	}
	free(d->dict);
	d->dict = NULL;
	d->size = 0;
	d->len = 0;
}

void	print_dict(t_dict *d)
{
	int	i;

	ft_putstr("Numbers:\n");
	i = 0;
	while (i < d->len)
	{
		if (d->dict[i].is_number)
		{
			ft_putnbr2(d->dict[i].number, " : ");
			ft_putstr2(d->dict[i].word, "\n");
		}
		i++;
	}
	ft_putstr("Magnitudes:\n");
	i = 0;
	while (i < d->len)
	{
		if (!d->dict[i].is_number)
		{
			ft_putnbr2(d->dict[i].number, " : ");
			ft_putstr2(d->dict[i].word, "\n");
		}
		i++;
	}
}
