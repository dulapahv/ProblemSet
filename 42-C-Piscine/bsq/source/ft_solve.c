/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_solve.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 02:16:08 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/29 17:34:05 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"

void	solve(t_map *map)
{
	reverse(map);
	back_traverse(map);
	find_max(map);
	find_ans_pos(map);
	swarm_row(map);
	swarm_col(map);
	adjust(map);
	adjust2(map);
	ft_arr_print(map);
}
