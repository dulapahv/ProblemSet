/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/21 13:43:48 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/21 13:52:01 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// n >= 46341 is for checking integer overflow.
// 46341 * 46341 will exceed integer limit
int	ft_sqrt(int nb)
{
	int	n;

	n = 1;
	if (nb > 0)
	{
		while (n * n <= nb)
		{
			if (n * n == nb)
				return (n);
			else if (n >= 46341)
				return (0);
			n++;
		}
	}
	return (0);
}
