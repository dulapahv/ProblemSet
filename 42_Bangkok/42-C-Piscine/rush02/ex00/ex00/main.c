/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tjukmong <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/26 12:55:12 by tjukmong          #+#    #+#             */
/*   Updated: 2022/06/26 12:58:52 by tjukmong         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "numdict.h"
#include "file_parser_util.h"
#include "file_parser.h"
#include "ft_main.h"
#include "ft_put.h"
#include "strcatm.h"

void	ft_parse_nbr(t_dict *dict, char *str, int len)
{
	int	nbr;

	ft_revchar(str, len);
	while (len)
	{
		nbr = str[len - 1] - 48;
		if (len % 3 == 0)
			ft_print_first(dict, str, nbr, len);
		else if (len % 3 == 2)
			ft_print_second(dict, str, nbr, len);
		else if (len % 3 == 1)
			ft_print_third(dict, str, nbr, len);
		len--;
	}
}

int	main(int argc, char **argv)
{
	t_dict	dict;

	create_dict(&dict);
	if (argc == 2)
	{
		file_parser("numbers.dict", &dict);
		ft_parse_nbr(&dict, argv[1], ft_strlen(argv[1]));
		ft_putstr("\n");
	}
	else if (argc == 3)
	{
		file_parser(argv[1], &dict);
		ft_parse_nbr(&dict, argv[1], ft_strlen(argv[1]));
		ft_putstr("\n");
	}
	else
		ft_putstr("Error\n");
	free_dict(&dict);
	return (0);
}
