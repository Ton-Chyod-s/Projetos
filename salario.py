
def salario(arg):
	num = int(arg)

	porcentagem = {
	'Despesas': 50, #50% do salario no mês seram para as despesas
	'Investimento': 30, #30% para os investimento tanto cursos como ativos
	'Fundo Emergencial': 10, #10% para emergencial caso aconteça algum sinisto na vida
	'Pode gastar': 10 #10% do salario vc podera gastar a toa, por que todo mundo tem direito a isso haha
	}

	for lin in porcentagem:
		pct = porcentagem[lin]/100
		res = num * pct
		print(lin,':',res)
	
	print('------------------------------------------')