/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: duvibuls <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/15 15:04:42 by duvibuls          #+#    #+#             */
/*   Updated: 2022/06/15 15:06:33 by duvibuls         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include "ft_strncat.c"

int	main(void)
{
	char dest[50] = "hello", dest2[50] = "hello";
	char *src;
	unsigned int size;
	size = 4;
	src = " test";
	printf("%s\n", strncat(dest, src, size));
	printf("%s\n", ft_strncat(dest2, src, size));
}

