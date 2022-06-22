/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   last_word.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/22 18:43:23 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/22 18:59:34 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	is_space(char c)
{
	if (c == ' ' || c == '\t')
		return (1);
	return (0);
}

void	last_word(char *str)
{
	int	i;
	int	start;

	i = 0;
	while (str[i] != '\0')
		i++;
	i -= 1;
	while (i >= 0 && is_space(str[i]))
		i--;
	start = i;
	while (i >= 0 && !is_space(str[i]))
		i--;
	i += 1;
	while (i <= start)
	{
		write(1, &str[i], 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		last_word(argv[1]);
	write(1, "\n", 1);
}
