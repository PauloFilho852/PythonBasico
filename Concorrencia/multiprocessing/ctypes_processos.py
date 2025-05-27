import multiprocessing
import time
import ctypes


def funcao1(valor, status):
    if status.value:
        result = valor.value + 10
        status.value = False
    else:
        result = valor.value + 20
        valor.value = 200
        status.value = True

    print(f'O resultado da funcao1 é {result}.')


def funcao2(valor, status):
    if status.value:
        result = valor.value + 30
        status.value = False
    else:
        result = valor.value + 40
        valor.value = 400
        status.value = True

    print(f'O resultado da funcao2 é {result}.')


def main():

    # Tipos que serão compartilhado entre os processos
    valor = multiprocessing.Value('i', 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target=funcao2, args=(valor, status))

    # Para consistência de resultado, não há concorrência
    p1.start()
    p1.join()

    p2.start()
    p2.join()


if __name__ == '__main__':
    main()
