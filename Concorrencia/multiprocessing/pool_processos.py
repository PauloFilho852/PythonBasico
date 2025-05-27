import multiprocessing


def calcular(dado):
    return dado ** 2


def imprimir_nome_processo():
    print(f'Processo: {multiprocessing.current_process().name}')


def main():
    tamanho_da_pool = multiprocessing.cpu_count()
    print(f'Tamanho da pool: {tamanho_da_pool}.')

    pool = multiprocessing.Pool(
        processes=tamanho_da_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))

    saidas = pool.map(calcular, entradas)

    pool.close()
    pool.join()

    print(f'Saidas: {saidas}')


if __name__ == '__main__':
    main()
