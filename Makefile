##
## EPITECH PROJECT, 2021
## 204 [WSL: Ubuntu]
## File description:
## Makefile
##

SRC	=	main.py

NAME	=	205IQ

all:	$(NAME)

$(NAME):
	@cp $(SRC) $(NAME)
	chmod 755 $(NAME)

clean:
	@echo "done"

fclean:	clean
	@rm -f $(NAME)
	@rm -f data

re:	fclean	all

test:	re
	@echo "\n=====Test1:=====\n"
	@-./$(NAME) -h
	@echo "\n=====Test2:=====\n"
	@-./$(NAME) 100 15 > data
	@head -n 2 data
	@echo ""
	@head -n 120 data | tail -n 10
	@echo ""
	@tail -n 2 data
	@echo "\n=====Test3:=====\n"
	@-./$(NAME) 100 24 90
	@echo "\n=====Test4:=====\n"
	@-./$(NAME) 100 24 90 95
	@echo "\n=====Test5:=====\n"
	@echo "You should get 12 errors:\n"
	@-./$(NAME) > /dev/null
	@-./$(NAME) 1 > /dev/null
	@-./$(NAME) a > /dev/null
	@-./$(NAME) 1 2 3 4 5 > /dev/null
	@-./$(NAME) 100 -1 > /dev/null
	@-./$(NAME) 100 24 -1 > /dev/null
	@-./$(NAME) 100 24 201 > /dev/null
	@-./$(NAME) 100 24 100 -1 > /dev/null
	@-./$(NAME) 100 24 100 201 > /dev/null
	@-./$(NAME) 100 24 100 a > /dev/null
	@-./$(NAME) 100 24 100 100 > /dev/null
	@-./$(NAME) 100 24 100 99 > /dev/null
	@echo "\nDone"
	@rm -f $(NAME)
	@rm -f data