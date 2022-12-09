/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotone.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 21:42:15 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/30 21:50:44 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	rot_13(char *str)
{
	int		i;
	char	c;

	i = 0;
	while (str[i])
	{
		if (str[i] >= 'a' && str[i] <= 'z')
		{
			c = (((str[i] - 'a') + 1) % 26) + 'a';
			write(1, &c, 1);
		}
		else if (str[i] >= 'A' && str[i] <= 'Z')
		{
			c = (((str[i] - 'A') + 1) % 26) + 'A';
			write(1, &c, 1);
		}
		else
			write(1, &str[i], 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc > 1)
		rot_13(argv[1]);
	write(1, "\n", 1);
}
