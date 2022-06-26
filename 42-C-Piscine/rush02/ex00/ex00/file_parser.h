/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utility.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 20:00:32 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/25 11:18:50 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FILE_PARSER_H
# define FILE_PARSER_H
# include "numdict.h"

void	rm_extra_space(char *str);
void	add_to_dict(t_dict *dict, int num, int is_number, char *word);
void	file_parser(char *file, t_dict *dict);

#endif
