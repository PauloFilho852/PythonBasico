# Doctests são testes colocados da docstrings de uma função
# para rodar o doctests deve ser dado comando: python -m doctest -v [modulename.py]
# Dentro da doctrins usa-se sempre aspas simples, tal como em 'a'.
def function(a, b):
    """
    Soma os números a e b
    >>> function(5,3)   
    8
    >>> function(5,5)
    7
    >>> function('a', 5)
    Traceback (most recent call last):
      ...
    TypeError: can only concatenate str (not "int") to str
    """
    return a + b


# soma = function(5, 3)
# print(f'Olá, Python!. Soma: {soma}')
