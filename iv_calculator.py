##### IV CALCULATOR POKEMON GO #####

print('''

	A Calculadora de IV a seguir informa o quanto seu Pokémon
	é perfeito. Você consegue descobrir o grau de perfeição
	indo no canto inferior direito da página do pokémon e 
	clicando em "Avaliar"

	Insira abaixo o nome do Pokémon e os resultados 
	da avaliação:

''')

print(' ')

pokemon = str(input('Pokémon: '))
attack = int(input('Ataque (0 - 15): '))
defense = int(input('Defesa (0 - 15): '))
stamina = int(input('Stamina (0 - 15): '))

iv_calc = ((attack + defense + stamina) * 100) / 45

print(f'O seu {pokemon} é {iv_calc:.1f} % perfeito')
