''' 
	1 Faça uma função que receba a altura inicial de uma árvore, 
      a taxa de crescimento ao ano e uma quantidade n de anos. 
      Esta função deve calcular altura desta árvore após n anos.
'''

class PrimeiroDesafio():
	"""docstring for PrimeiroDesafio"""
	def __init__(self):
		super(PrimeiroDesafio, self).__init__()
		# self.arg = arg
		

	def altura_arvore(altura, taxa_crescimento, qta_ano):
		calculo = altura * ((taxa_crescimento / 100) * qta_ano)
		print(f'A altura atual da arvore é {altura}, com a taxa de crescimento de {taxa_crescimento}% a cada {qta_ano} anos, '
	      f'a altura desta arvore será {(calculo + altura)}')
	

if __name__ == '__main__':
	desafio = PrimeiroDesafio()
	desafio.altura_arvore(1000,40,20)

