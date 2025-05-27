import threading


class Exemplo:
    def __init__(self):
        self.lock = threading.RLock()
        self.valor = 0

    def metodo_externo(self):
        with self.lock:
            self.valor += 1
            self.metodo_interno()

    def metodo_interno(self):
        with self.lock:  # A mesma thread pode adquirir o lock novamente, sem causar deadlok
            self.valor += 1


obj = Exemplo()


def executar():
    for _ in range(10000):
        obj.metodo_externo()


t1 = threading.Thread(target=executar)
t2 = threading.Thread(target=executar)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Valor final: {obj.valor}")
