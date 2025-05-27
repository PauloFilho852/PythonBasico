import multiprocessing
import time
import ctypes
import colorama

colorama.init()

lock = multiprocessing.Lock()


def funcao1(valor, lock):
    with lock:
        temp = valor.value
        time.sleep(0.01)
        valor.value = temp + 200


def funcao2(valor, lock):
    with lock:
        temp = valor.value
        time.sleep(0.01)
        valor.value = temp - 200


def main():

    # Tipo que será compartilhado entre os processos
    valor = multiprocessing.Value('i', 100)

    print(colorama.Fore.WHITE + f'Valor inicial: {valor.value}.')

    p1 = multiprocessing.Process(target=funcao1, args=(valor, lock))
    p2 = multiprocessing.Process(target=funcao2, args=(valor, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    valor_esperado = 100

    if valor_esperado == valor.value:
        print(colorama.Fore.GREEN +
              f'ACERTO. Valor final: {valor.value}. Valor esperado: {valor_esperado}')
    else:
        print(colorama.Fore.RED +
              f'ERRO. Valor final: {valor.value}. Valor esperado: {valor_esperado}')


if __name__ == '__main__':
    for i in range(100):
        main()
        print('\n')
        time.sleep(0.5)
