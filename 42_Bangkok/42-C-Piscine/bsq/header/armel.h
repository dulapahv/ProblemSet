/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   header.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/27 20:31:36 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/27 20:31:38 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef ARMEL_H
# define ARMEL_H
# include <fcntl.h>
# include <stdlib.h>
# include <unistd.h>
#include <stdio.h>
#define D printf("OK\n");
typedef struct s_map
{
	int		row;
	int		col;
	int		max;
	int		**arr;
	int		**obs_pos;
	int		*ans_pos_start;
	int		*ans_pos_end;
	char	obs;
	char	free;
	char	square;
}	t_map;

/*** ft_readfile.c ***/
char	*ft_readfile(char *file_name);

/*** ft_locate_obs.c ***/
int	ft_fill_obs(t_map *pmap, char **box);

/*** ft_spilt.c ***/
char	**ft_split(char *str, char spliter);

/*** ft_utility.c ***/
int		ft_strlen(char *str);
int		ft_atoi(char *str);
void	ft_putstr(char *str);

/*** ft_map_utility.c ***/
t_map	*ft_create_map(char *content);

/*** ft_god_of_free.c ***/
void    ft_free_box(char ***box);
void	ft_free_arr(t_map *map);
void	ft_free_complete_map(t_map **map);

/*** ft_check_file.c ***/
int ft_check_file(char *content);

/*** ft_string.c ***/
int	ft_ptr_strlen(char **str, char c);
int	ft_nptr_strlen(char *str, char c);
int	ft_wordcount(char *str, char c);
int	ft_is_not_printable(char *str, char not);
int	ft_is_same(char *str);

/*** ft_solve_utility.c ***/
void	reverse(t_map *map);
int		min3(int a, int b, int c);
void	back_traverse(t_map *map);
void	find_max(t_map *map);
int		find_ans_pos(t_map *map);

/*** ft_solve_utility2.c ***/
int		swarm_row(t_map *map);
int		swarm_col(t_map *map);
void	adjust(t_map *map);
void	adjust2(t_map *map);
void    ft_arr_print(t_map *map);

/*** ft_solve.c ***/
void	solve(t_map *map);

#endif