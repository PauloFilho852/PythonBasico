# from concurrent.futures.thread import ThreadPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time


def tarefa_pesada(n):
    print(f"Processando {n}...")
    time.sleep(2)
    return n * n


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]

    executor = ProcessPoolExecutor(max_workers=3)

    # Mapeia a função para os valores
    resultados = list(executor.map(tarefa_pesada, numeros))

    # Força o encerramento dos processos após o término das tarefas
    executor.shutdown(wait=True)

    print("Resultados:", resultados)
