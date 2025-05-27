import threading
import time
import colorama

contador = 0
lock = threading.Lock()


def incrementar():
    global contador
    for _ in range(100):
        with lock:  # Garante que apenas uma thread acesse o contador por vez
            valor_atual = contador
            time.sleep(0.001)  # Força a chance de troca de contexto
            contador = valor_atual + 1


# Criando threads
t1 = threading.Thread(target=incrementar)
t2 = threading.Thread(target=incrementar)

# Iniciando threads
t1.start()
t2.start()
t1.join()
t2.join()

valor_esperado = 200

if contador != valor_esperado:
    print(colorama.Fore.RED +
          f"ERRO. Contador: {contador}. Valor Esperado: {valor_esperado}", flush=True)
else:
    print(colorama.Fore.BLUE +
          f"OK. Contador: {contador}. Valor Esperado: {valor_esperado}", flush=True)

print(colorama.Fore.WHITE + 'Pronto.')


# Outra forma de usar do lock

# lock.acquire() # Faz o lock

# Sessão crítica.

# lock.release() # Liberad o lock
