import multiprocessing


def fazer_algo(valor):
    print(f'Fazendo algo com o {valor}')


def main():
    print(
        f'Iniciando a aplicação com o processo {multiprocessing.current_process().name}.')

    pc = multiprocessing.Process(
        target=fazer_algo, args=('Passaro',), name='MeuProcesso')
    print(f'Iniciando o processo {pc.name}.')
    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
