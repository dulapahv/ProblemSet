/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   file_parser.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 20:00:32 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/25 12:50:20 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include "file_parser_util.h"
#include "ft_put.h"
#include "numdict.h"
#include "utility.h"

void	rm_extra_space(char *str)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	if (str == NULL)
		error();
	while (str[i])
	{
		if (str[i] == ' ' && str[i + 1] == ' ')
		{
			i++;
			continue ;
		}
		str[j++] = str[i++];
	}
	str[j] = '\0';
}

void	add_to_dict(t_dict *dict, int num, int is_number, char *word)
{
	if (word != NULL && dict != NULL)
	{
		if (is_number == 1)
			add_num(dict, num, word);
		else if (is_number == 0)
			add_mag(dict, num, word);
		free(word);
	}
	else
		error();
}

void	file_parser(char *file, t_dict *dict)
{
	int		fp;
	int		num;
	int		is_number;
	char	c[1];
	char	*word;

	c[0] = 0;
	num = 0;
	word = NULL;
	is_number = 0;
	fp = open(file, O_RDONLY);
	if (fp == -1)
		error();
	while (read(fp, c, 1))
	{
		word = NULL;
		num = get_nbr(fp, c, &is_number);
		word = get_word(fp, c);
		rm_extra_space(word);
		add_to_dict(dict, num, is_number, word);
	}
}
/*
int	main(void)
{	
	t_dict	*d;

	d = malloc(sizeof(t_dict));
	create_dict(d);
	file_parser("numbers.dict", d);
	print_dict(d);
	free_dict(d);
	free(d);
}
*/
