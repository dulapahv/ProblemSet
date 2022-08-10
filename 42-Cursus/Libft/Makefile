# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: duvibuls <duvibuls@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/10 17:20:23 by duvibuls          #+#    #+#              #
#    Updated: 2022/08/10 17:20:23 by duvibuls         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

DIRSRC			= ./

SRC				= ft_memset.c ft_bzero.c ft_memcpy.c ft_memmove.c\
				ft_memchr.c ft_memcmp.c ft_strlen.c ft_isalpha.c\
				ft_isdigit.c ft_isalnum.c ft_isascii.c ft_isprint.c\
				ft_toupper.c ft_tolower.c ft_strchr.c ft_strrchr.c\
				ft_strncmp.c ft_strlcpy.c ft_strlcat.c ft_strnstr.c\
				ft_atoi.c ft_calloc.c ft_strdup.c ft_substr.c\
				ft_strjoin.c ft_strtrim.c ft_split.c ft_itoa.c\

SRCS			= ${addprefix ${DIRSRC}, ${SRC}}

OBJS			= ${SRCS:.c=.o}

HEAD			= .

NAME			= libft.a

CC				= gcc

RM				= rm -f

CFLAGS			= -Wall -Wextra -Werror

.c.o:
	@${CC} ${CFLAGS} -c -I ${HEAD} $< -o ${<:.c=.o} -std=c99

all:			${NAME}
	# @${CC} ${OBJS} -o ${NAME:.a=.out} -lbsd && ./${NAME:.a=.out}

${NAME}:	${OBJS}
			ar rc ${NAME} ${OBJS}

clean:
			${RM} ${OBJS}

fclean:		clean
			${RM} ${NAME}

re:			fclean all

.PHONY:		all clean fclean re

