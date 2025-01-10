# pip install mypy
# executando o arquivo com mypy há verificação de tipos

# Type Hinting está definido no comentário dentro da função
def function(a, b):
    # type: (str, int) -> str
    c: int = int(a) + b
    return c


# Type Hinting em declaração de variáveis
x: str = '10'
y: int = 5
z: bool = False

print(function(True, y))

# Definindo um novo tipo para variável x.
x = True

print(z)

print(function.__annotations__)  # Exibindo os tipos de parâmetros
