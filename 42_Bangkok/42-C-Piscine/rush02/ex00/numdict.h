/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   numdict.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: abossel <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 19:59:35 by abossel           #+#    #+#             */
/*   Updated: 2022/06/24 22:56:57 by abossel          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef NUMDICT_H
# define NUMDICT_H

# define DICT_SIZE 50

typedef struct s_dict_elem
{
	int		number;
	int		is_number;
	char	*word;
}	t_dict_elem;

typedef struct s_dict
{
	t_dict_elem	*dict;
	int			size;
	int			len;
}	t_dict;

int		create_dict(t_dict *d);
int		extend_dict(t_dict *d);
void	free_dict(t_dict *d);
void	print_dict(t_dict *d);
void	add_num(t_dict *d, int num, char *str);
void	add_mag(t_dict *d, int mag, char *str);
char	*get_num_word(t_dict *d, int num);
char	*get_mag_word(t_dict *d, int mag);

#endif
