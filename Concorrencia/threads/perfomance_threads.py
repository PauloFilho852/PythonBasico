import threading
import time

# Uso de threading pode melhorar multiplas tafefas I/O-bound.


def tarefa_io(i):
    print(f"Tarefa {i} iniciada")
    time.sleep(2)  # Simula operação I/O
    print(f"Tarefa {i} finalizada")


# Execução SEQUENCIAL
inicio_seq = time.perf_counter()
for i in range(5):
    tarefa_io(i)
fim_seq = time.perf_counter()
print(f"Tempo total sequencial: {fim_seq - inicio_seq:.2f} segundos\n")

# Execução com THREADS
threads = []
inicio_thread = time.perf_counter()
for i in range(5):
    t = threading.Thread(target=tarefa_io, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
fim_thread = time.perf_counter()
print(f"Tempo total com threads: {fim_thread - inicio_thread:.2f} segundos")
