/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/27 20:30:23 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/29 16:51:44 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

int	msg_error(void)
{
	write(1, "Error\n", 6);
	return (0);
}

int	ft_if_fail(t_map *pmap, char *content)
{
	int	flag;

	flag = (int)(!content || ft_check_file(content) || !pmap);
	if (!content)
		write(1, "Error\n", 6);
	if (ft_check_file(content) || !pmap)
	{
		write(1, "Error\n", 6);
		free(content);
	}
	return (flag);
}

void	ft_run_program(int argc, char **argv)
{
	int		i;
	char	*content;
	t_map	*map;

	i = 0;
	while (i < argc - 1)
	{
		content = ft_readfile(argv[i]);
		if (content != NULL)
		{
			map = ft_create_map(content);
			if (!ft_if_fail(map, content))
			{
				solve(map);
				ft_free_complete_map(&map);
				free(content);
			}
		}
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc < 2)
		return (msg_error());
	ft_run_program(argc, &argv[1]);
	return (0);
}
