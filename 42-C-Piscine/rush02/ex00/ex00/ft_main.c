/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_main.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tjukmong <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/26 12:54:22 by tjukmong          #+#    #+#             */
/*   Updated: 2022/06/26 12:58:23 by tjukmong         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "numdict.h"
#include "ft_put.h"
#include <stdio.h>

void	ft_revchar(char *tab, int size)
{
	int	t1;
	int	t2;
	int	loop;
	int	oldsize;

	oldsize = size;
	loop = size;
	while (size > loop / 2)
	{
		t1 = tab[oldsize - size];
		t2 = tab[size - 1];
		tab[oldsize - size] = t2;
		tab[size - 1] = t1;
		size--;
	}
}

int	ft_all_zeros(char *str, int indx)
{
	while (str[--indx] == '0')
		continue ;
	return (indx);
}

// First (digit + mag + "and") Eg: "two hundred and", "and one hundred"
void	ft_print_first(t_dict *dict, char *str, int nbr, int ptr)
{
	if (nbr != 0)
	{
		ft_putstr(get_num_word(dict, nbr));
		ft_putstr2(" ", get_num_word(dict, 100));
	}
	if (ft_all_zeros(str, ptr + 3) && ptr > 3)
		ft_putstr(" and ");
}

// Second (digit (with postfix)) Eg: "twelve-thousand, ", or "twenty-"
void	ft_print_second(t_dict *dict, char *str, int nbr, int ptr)
{
	if (nbr == 1)
		ft_putstr(get_num_word(dict, str[ptr - 2] - 48 + 10));
	else if (ptr != 1 && nbr != 0)
		ft_putstr(get_num_word(dict, nbr * 10));
	if (str[ptr - 1] > '1' && str[ptr - 2] > '0')
		ft_putstr("-");
}

// (digit + mag) Eg: "three thousand, " or "three" 
void	ft_print_third(t_dict *dict, char *str, int nbr, int ptr)
{
	if (str[ptr] != '1' && nbr != 0)
	{
		ft_putstr2(" ", get_num_word(dict, nbr));
	}
	if (ptr != 1 && ft_all_zeros(str, ptr + 3))
	{
		ft_putstr2(" ", get_mag_word(dict, (ptr / 3) * 3));
		if (ptr != 3)
			ft_putstr(", ");
	}
	if (ptr == 1 && str[0] == *"0" && str[1] == 0)
		ft_putstr(get_num_word(dict, 0));
}
