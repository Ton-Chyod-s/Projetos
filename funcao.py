#def para fazer calculos matematicos +, - , * , /
def calc(arg):
	usuario = str(arg)
 
	try:
		conta = eval(usuario)
		print(f'o resultado é:\t{conta}')
	except:
		print(f'conta invalida')
  
if __name__ == '__main__':
	calc(5 * 2)
	
		