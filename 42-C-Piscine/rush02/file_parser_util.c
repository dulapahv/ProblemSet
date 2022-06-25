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
#include "utility.h"
#include "numdict.h"

int	nbr_chk_flag(int flag, char *str_num, int index, int *is_number)
{
	int	num;

	num = 0;
	if (flag == 1)
	{
		str_num[index] = '\0';
		num = ft_atoi(str_num);
		*is_number = 1;
		free(str_num);
	}
	else if (flag == 2)
	{
		str_num[index] = '\0';
		num = index - 1;
		*is_number = 0;
		free(str_num);
	}
	else
		error();
	return (num);
}

int	get_nbr(int fp, char c[1], int *is_number)
{
	int		flag;
	char	*temp;
	int		i;

	flag = 0;
	temp = NULL;
	i = 0;
	if (is_numeric(c[0]))
	{
		temp = malloc(sizeof(char) * 1024);
		if (!temp)
			error();
		flag = 1;
		while (c[0] != ':' && c[0] != ' ' && c[0] != '\t')
		{
			if (!is_numeric(c[0]))
				error();
			temp[i++] = c[0];
			if (i > 3)
				flag = 2;
			read(fp, c, 1);
		}
	}
	return (nbr_chk_flag(flag, temp, i, is_number));
}

void	skip(int fp, char c[1])
{
	if (fp == -1 || c == NULL)
		error();
	while (c[0] == ' ' || c[0] == '\t')
		read(fp, c, 1);
	if (c[0] == ':')
		read(fp, c, 1);
	while (c[0] == ' ' || c[0] == '\t')
		read(fp, c, 1);
}

char	*word_chk_flag(int flag, char *str, int index)
{
	char	*word;

	word = NULL;
	if (flag == 3)
	{
		str[index] = '\0';
		word = ft_strdup(str);
		free(str);
	}
	return (word);
}

char	*get_word(int fp, char c[1])
{
	char	*temp;
	int		flag;
	int		is_not_eof;
	int		i;

	temp = NULL;
	flag = 0;
	is_not_eof = 0;
	i = 0;
	skip (fp, c);
	if (is_printable(c[0]))
	{
		temp = malloc(sizeof(char) * 2048);
		if (!temp)
			error();
		flag = 3;
		while (c[0] != '\n')
		{
			temp[i++] = c[0];
			is_not_eof = read(fp, c, 1);
			if (!is_not_eof)
				break ;
		}
	}
	return (word_chk_flag(flag, temp, i));
}
