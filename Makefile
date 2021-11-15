##
## EPITECH PROJECT, 2020
## groundhog
## File description:
## Makefile
##

SRC	=	ducks.py

NAME	=	204ducks

$(NAME):
			cp $(SRC) 204ducks
			chmod +x 204ducks

all:	$(NAME)

clean:
		rm -rf 204ducks

fclean:	clean

re:	fclean all