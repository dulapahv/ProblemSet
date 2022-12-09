/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   first_word.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 19:40:10 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/30 19:54:38 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	is_space(char c)
{
	if (c == ' ' || c == '\t')
		return (1);
	return (0);
}

void	first_word(char *str)
{
	int	i;
	int	chk;

	i = 0;
	while (is_space(str[i]) && str[i] != '\0')
		i++;
	chk = i;
	while (!is_space(str[i]) && str[i] != '\0' && chk != 0)
	{
		write(1, &str[i], 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc > 1)
		first_word(argv[1]);
	write(1, "\n", 1);
}
