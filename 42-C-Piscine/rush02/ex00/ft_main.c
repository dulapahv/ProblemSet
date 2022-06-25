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

// First (digit + mag + "and") Eg: "two hundred and", "and one hundred"
void	ft_print_first(t_dict *dict, char* str, int nbr, int len)
{
	ft_putstr("|\x1b[1;31m");
	if (!(str[len - 2] != '0' || str[len - 3] != '0') && len == 4)
		ft_putstr("and ");
	if (nbr != 0)
	{
		ft_putstr(get_num_word(dict, nbr));
		ft_putstr2(" ", get_num_word(dict, 100));
	}
	if (str[len - 2] != '0' || str[len - 3] != '0')
		ft_putstr(" and ");
}

// Second (digit (with postfix)) Eg: "twelve-thousand, ", or "twenty-"
void	ft_print_second(t_dict *dict, char *str, int nbr, int len)
{
	ft_putstr("|\x1b[1;32m");
	if (nbr == 1)
		ft_putstr(get_num_word(dict, str[len - 2] - 48 + 10));
	else if (len != 1 && nbr != 0)
		ft_putstr(get_num_word(dict, nbr * 10));
	if (str[len - 1] > '1' && str[len - 2] > '0')
		ft_putstr("-");
}

// (digit + mag) Eg: "three thousand, " or "three" 
void	ft_print_third(t_dict *dict, char *str, int nbr, int len)
{
	ft_putstr("|\x1b[1;34m");

	if (str[len] != '1' && nbr != 0)
	{
		ft_putstr(get_num_word(dict, nbr));
	}
	if (len != 1 && ((str[len + 1] != '0' && str[len + 2] != '0') || len % 4))
	{
		ft_putstr2(" ", get_mag_word(dict, len / 3));
		ft_putstr(", ");
	}
	if (len == 1 && str[0] == *"0" && str[1] == 0)
		ft_putstr(get_num_word(dict, 0));
}