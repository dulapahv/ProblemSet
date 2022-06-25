/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utility.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/24 20:00:32 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/25 11:18:59 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef UTILITY_H
# define UTILITY_H

int		ft_atoi(char *str);
char	*ft_strdup(char *src);
int	is_numeric(char c);
int is_printable(char c);
int error(void);

#endif
