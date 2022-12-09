/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_main.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tjukmong <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/26 12:54:48 by tjukmong          #+#    #+#             */
/*   Updated: 2022/06/26 13:00:12 by tjukmong         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_MAIN_H
# define FT_MAIN_H
# include "numdict.h"

void	ft_revchar(char *tab, int size);
void	ft_print_first(t_dict *dict, char *str, int nbr, int ptr);
void	ft_print_second(t_dict *dict, char *str, int nbr, int ptr);
void	ft_print_third(t_dict *dict, char *str, int nbr, int ptr);

#endif
