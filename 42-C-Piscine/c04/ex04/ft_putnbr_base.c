/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/19 14:58:14 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/19 15:12:50 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	re_putnbr_base(int nbr, char *base, int size)
{
	unsigned int	n;
	char			c;

	if (nbr < 0)
	{
		write(1, "-", 1);
		n = nbr * (-1);
	}
	else
		n = nbr;
	if (n >= (unsigned int)size)
		re_putnbr_base(n / size, base, size);
	c = base[n % size];
	write(1, &c, 1);
}

int	verify(char *base)
{
	int	i;

	i = 0;
	while (base[i] != '\0')
	{
		if (base[i] == '+' || base[i] == '-' || base[i] == base[i + 1])
			return (0);
		i++;
	}
	if (i <= 1)
		return (0);
	return (1);
}

void	ft_putnbr_base(int nbr, char *base)
{
	int	i;

	i = 0;
	if (verify(base) == 1)
	{
		while (base[i] != '\0')
			i++;
		re_putnbr_base(nbr, base, i);
	}
}
