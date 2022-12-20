#def para fazer calculos matematicos +, - , * , /
def calc(arg):
	usuario = str(arg)
	conta = eval(usuario)
	print(f'o resultado é:\t{conta}')


if __name__ == '__main__':
	calc(5 * 2)
	
		