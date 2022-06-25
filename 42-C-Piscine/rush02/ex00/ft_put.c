/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: abossel <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/14 21:23:10 by abossel           #+#    #+#             */
/*   Updated: 2022/06/25 13:32:07 by abossel          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr(char *str)
{
	if (str == 0)
		return ;
	while (*str != '\0')
	{
		write(1, str, 1);
		str++;
	}
}

void	ft_putstr2(char *s1, char *s2)
{
	ft_putstr(s1);
	ft_putstr(s2);
}

void	ft_putnbr(int nb)
{
	int		div;
	int		mod;
	char	c;

	div = nb / 10;
	mod = nb % 10;
	if (nb < 0)
	{
		write(1, "-", 1);
		div = -div;
		mod = -mod;
	}
	if (div != 0)
	{
		ft_putnbr(div);
	}
	c = '0' + mod;
	write(1, &c, 1);
}

void	ft_putnbr2(int nb, char *str)
{
	ft_putnbr(nb);
	ft_putstr(str);
}
