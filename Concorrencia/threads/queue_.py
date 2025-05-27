import time
import colorama

from threading import Thread
from queue import Queue

colorama.init()


def gerador_de_dados(queue: Queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dado {i} gerado.', flush=True)
        queue.put(i)
        time.sleep(1)


def conusmidor_de_dados(queue: Queue):
    while queue.qsize() > 0:
        # O get aguarda até que um dado esteja na queue.
        # Caso as threads fossem concorrentes, a condição do laço poderia provocar
        # a não execução do threcho abaixo.
        valor = queue.get()
        print(colorama.Fore.RED + f'Dado {valor} consumido.', flush=True)
        queue.task_done()
        time.sleep(1)


print(colorama.Fore.WHITE + 'Sistema iniciado.', flush=True)

queue = Queue()

th1 = Thread(target=gerador_de_dados, args=(queue,))
th2 = Thread(target=conusmidor_de_dados, args=(queue,))

# As threads não são concorrentes.
th1.start()
th1.join()

th2.start()
th2.join()
