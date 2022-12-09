SRC	= ./source/ft_check_file.c ./source/ft_map_utility.c ./source/ft_readfile.c ./source/ft_solve.c ./source/ft_split.c ./source/ft_string.c ./source/ft_utility.c ./source/ft_solve_utility.c ./source/ft_solve_utility2.c ./source/ft_god_of_free.c ./source/ft_locate_obs.c ./source/vlad.c 

NAME	= bsq

INCDIR	= ./header/

CC	= gcc

CFLAGS	= -Wall -Wextra -Werror -g

RM	= rm -f

.c.o:
	@${CC} ${CFLAGS} -I${INCDIR} -c $< -o ${<:.c=.o}

${NAME}:	${SRC}
	@${CC} ${CFLAGS} -o ${NAME} ${SRC}

all:	${NAME}

clean:
	@${RM} ${OBJS}

fclean: clean
	@${RM} ${NAME}

re:	fclean all

.PHONY:	all clean fclean re
