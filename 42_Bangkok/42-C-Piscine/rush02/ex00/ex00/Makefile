SRCLIST	= main.c ft_main.c numdict.c numdict2.c ft_put.c utility.c file_parser.c file_parser_util.c strcatm.c

SRCDIR	= ./

NAME	= rush02

SRCS	= ${addprefix ${SRCDIR}, ${SRCLIST}}

OBJS	= ${SRCS:.c=.o}

INCDIR	= ./

CC	= gcc

CFLAGS	= -Wall -Wextra -Werror

RM	= rm -f

.c.o:
	${CC} ${CFLAGS} -I${INCDIR} -c $< -o ${<:.c=.o}

${NAME}:	${OBJS}
	${CC} ${CFLAGS} -o ${NAME} ${OBJS}

all:	${NAME}

clean:
	${RM} ${OBJS}

fclean: clean
	${RM} ${NAME}

re:	fclean all

.PHONY:	all clean fclean re
