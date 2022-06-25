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

#ifndef FILE_PARSER_UTIL_H
# define FILE_PARSER_UTIL_H

int		nbr_chk_flag(int flag, char *str_num, int index, int *is_number);
int		get_nbr(int fp, char c[1], int *is_number);
void	skip(int fp, char c[1]);
char	*word_chk_flag(int flag, char *str, int index);
char	*get_word(int fp, char c[1]);

#endif
