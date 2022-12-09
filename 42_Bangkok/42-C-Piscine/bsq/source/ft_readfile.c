/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_readfile.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tponutha <tponutha@student.42bangkok.com>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/28 17:00:35 by tponutha          #+#    #+#             */
/*   Updated: 2022/06/29 16:50:21 by tponutha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/armel.h"
#define BUFFER 10240

void	*ft_error(void)
{
	write(1, "Error\n", 6);
	return (NULL);
}

char	*ft_delete_useless_line(char *str, int endline)
{
	int	i;

	i = endline;
	while (str[i] < 32 || str[i] == 127)
	{
		str[i] = 0;
		i--;
	}
	return (str);
}

char	*ft_readfile(char *file_name)
{
	int		fd;
	int		filelen;
	char	*content;

	content = (char *)malloc(sizeof(char) * BUFFER + 1);
	if (!content)
		return (ft_error());
	fd = open(file_name, O_RDONLY);
	if (fd == -1)
	{
		free(content);
		return (ft_error());
	}
	filelen = read(fd, content, BUFFER);
	content = ft_delete_useless_line(content, filelen);
	return (content);
}
/*
#include <stdio.h>
int	main()
{
	char *a = ft_readfile("map1");
	printf("%s\n", a);
}
*/
