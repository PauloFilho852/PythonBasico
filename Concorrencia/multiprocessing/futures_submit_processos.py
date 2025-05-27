from concurrent.futures import ProcessPoolExecutor
import time


def tarefa(n):
    time.sleep(1)
    return n * n


if __name__ == "__main__":
    # max_workers indica quantos processo serão executados por vez.
    with ProcessPoolExecutor(max_workers=4) as executor:
        futuros = [executor.submit(tarefa, i) for i in range(4)]

        for futuro in futuros:
            print(f"Resultado: {futuro.result()}")
