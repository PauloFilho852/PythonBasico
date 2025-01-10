# import pdb

# Comandos básicos do PDB
# l ->lista onde estamos no código
# n ->próxima linha
# p [var_name]->imprime variável
# c ->continua a execução (finaliza o debug)
# [var_name]->imprime variável

nome = 'Angelina'
sobrenome = 'Jolie'

breakpoint()  # breakpoint a partir do Python 3.7
# pdb.set_trace() #breakpoint

nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso' + curso
print(final)
