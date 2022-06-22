/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   inter.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/22 11:36:12 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/22 11:56:13 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	inter(char *find, char *src)
{
	int	*arr;
	int	i;

	arr = (int [127]){0};
	i = 0;
	while (src[i] != '\0')
	{
		arr[(int)src[i]]++;
		i++;
	}
	i = 0;
	while (find[i] != '\0')
	{
		if (arr[(int)find[i]] != 0)
		{
			write(1, &find[i], 1);
			arr[(int)find[i]] = 0;
		}
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 3)
		inter(argv[1], argv[2]);
	write(1, "\n", 1);
}
