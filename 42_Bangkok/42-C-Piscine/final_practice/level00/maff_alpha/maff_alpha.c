/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   maff_alpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 15:59:59 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/30 16:06:21 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(void)
{
	char	lower;
	char	upper;
	int		i;

	lower = 'a';
	upper = 'A';
	i = 0;
	while (i < 26)
	{
		if (i % 2 == 0)
			write(1, &lower, 1);
		else
			write(1, &upper, 1);
		lower++;
		upper++;
		i++;
	}
}
