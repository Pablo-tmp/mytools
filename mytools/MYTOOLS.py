PI_INT = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
E_INT = 7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

def pi_real(n: int) -> str:
	"""
		Recebe um número natural maior que 0 e menor que 100 e retorna
		uma aproximação de PI com n casas decimais.
	"""

	return f'3,{str(PI_INT)[:n]}'

def e_real(n: int) -> str:
	"""
		Recebe um número natural maior que 0 e menor que 100 e retorna
		uma aproximação para o número neperiano com n casas decimais.
	"""

	return f'2,{str(E_INT)[:n]}'
