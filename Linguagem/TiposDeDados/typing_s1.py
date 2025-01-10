# Os tipos declarados com as classes do módulo typing podem ser verificados com o mypy.

from typing import List, Tuple

combinacao: Tuple[str, str] = ('a', '1')

print(combinacao)

# Com as classes do módulo typing é possícel guardar a declarar de tipo em um objeto
tipo = List[str]

combinacao: tipo = [('a', '2')]

print(combinacao)
