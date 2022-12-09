/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/19 15:46:01 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/19 23:58:42 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	verify(char *base)
{
	int	i;

	i = 0;
	while (base[i] != '\0')
	{
		if (base[i] == '+' || base[i] == '-' || base[i] == base[i + 1]
			|| base[i] == ' ' || base[i] == '\n' || base[i] == '\t'
			|| base[i] == '\v' || base[i] == '\f' || base[i] == '\r')
			return (0);
		i++;
	}
	if (i <= 1)
		return (0);
	return (1);
}

int	ft_multiply_nbr(char d, char *base, int multiple, int nbr)
{
	int	c;

	c = 0;
	while (base[c] != '\0')
	{
		if (d == base[c])
			return (nbr + (multiple * c));
		c++;
	}
	return (nbr);
}

int	ft_isbase(char n, char *base)
{
	int	c;

	c = 0;
	if (n == '+' || n == '-' || n == '\v' || n == '\f' || n == '\r'
		|| n == ' ' || n == '\t' || n == '\n')
		return (1);
	while (base[c] != '\0')
	{
		if (base[c] == n)
			return (2);
		c++;
	}
	return (0);
}

int	ft_atoi(char *str, char *base, int size, int start)
{
	int	c;
	int	s;
	int	res;
	int	mult;

	c = start - 1;
	s = 1;
	res = 0;
	mult = 1;
	while (c >= 0)
	{
		if (str[c] == '-')
			s *= (-1);
		if (ft_isbase(str[c], base) == 2)
		{
			res = ft_multiply_nbr(str[c], base, mult, res);
			mult *= size;
		}
		c--;
	}
	return (res * s);
}

int	ft_atoi_base(char *str, char *base)
{
	int	size;
	int	c;

	size = 0;
	c = 0;
	if (verify(base) == 0)
		return (0);
	while (base[size] != '\0')
		size++;
	while (str[c] == '\n' || str[c] == '\t' || str[c] == '\v'
		|| str[c] == '\f' || str[c] == '\r' || str[c] == ' ')
		c++;
	while (str[c] == '-' || str[c] == '+')
		c++;
	while (str[c] >= '0' && str[c] <= '9')
		c++;
	return (ft_atoi(str, base, size, c));
}
