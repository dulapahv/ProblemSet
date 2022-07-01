/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_print.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 21:19:59 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/30 21:38:11 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	rev_print(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	while (i--)
		write(1, &str[i], 1);
}

int	main(int argc, char **argv)
{
	if (argc > 1)
		rev_print(argv[1]);
	write(1, "\n", 1);
}
