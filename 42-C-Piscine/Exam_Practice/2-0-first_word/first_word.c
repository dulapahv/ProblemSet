/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   first_word.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/22 11:10:03 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/22 11:25:47 by duvibuls         ###   ########.fr       */
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
	int	start;

	i = 0;
	while (str[i] != '\0' && is_space(str[i]))
		i++;
	start = i;
	while (str[i] != '\0' && !is_space(str[i]))
		i++;
	while (start < i && i != 1)
	{
		write(1, &str[start], 1);
		start++;
	}
}

int	main(int argc, char **argv)
{
	if (argc > 1)
	{
		first_word(argv[1]);
	}
	write(1, "\n", 1);
}
