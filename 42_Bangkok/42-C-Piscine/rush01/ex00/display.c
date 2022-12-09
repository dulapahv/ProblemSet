#include "headers.h"
#include <unistd.h>

void	ft_putchar(char c)
{
	write (1, &c, 1);
	return ;
}

void	ft_putstr(char *str)
{
	int	n;

	n = 0;
	while (str[n])
		ft_putchar(str[n++]);
	return ;
}