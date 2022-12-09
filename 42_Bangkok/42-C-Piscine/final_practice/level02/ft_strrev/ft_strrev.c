/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <duvibuls@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 23:27:33 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/30 23:43:21 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strrev(char *str)
{
	char	*start;
	char	*end;
	char	tmp;
	int		len;
	int		j;

	len = 0;
	while (str[len])
		len++;
	start = str;
	end = str;
	j = 0;
	while (j < len - 1)
	{
		end++;
		j++;
	}
	j = 0;
	while (j < len / 2)
	{
		tmp = *end;
		*end = *start;
		*start = tmp;
		j++;
		start++;
		end--;
	}
	return (str);
}
