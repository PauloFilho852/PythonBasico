num1 = 50
num2 = 50

def somar(a, b):
    return a + b

#Em Python, caso o módulo for o módulo de chamada do programa, o atributo __name__ é 
#atribuido o valor '__main__'.

if __name__ == '__main__':
    print(somar(num1,num2))
    print(__name__)
else:
    print(somar(num1, num2))
    print(__name__)