/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   maff_revalpha.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 15:59:59 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/30 16:08:49 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(void)
{
	char	lower;
	char	upper;
	int		i;

	lower = 'z';
	upper = 'Z';
	i = 25;
	while (i >= 0)
	{
		if (i % 2 == 1)
			write(1, &lower, 1);
		else
			write(1, &upper, 1);
		lower--;
		upper--;
		i--;
	}
}
