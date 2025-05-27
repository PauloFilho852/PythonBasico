import asyncio
import threading
import time

# Função que simula atividade contínua na thread principal
def contador():
    for i in range(10):
        print(f"[Thread Principal] Contando: {i}")
        time.sleep(0.5)  # Simula trabalho da thread principal

# Função assíncrona simulando uma tarefa que "espera"
async def diz_oi():
    print("[Assíncrono] Oi")
    await asyncio.sleep(3)  # Pausa assíncrona (não bloqueia a thread)
    print("[Assíncrono] Fim")

# Função principal do asyncio
async def main():
    await diz_oi()

# Inicia a thread paralela que executa o contador
contador_thread = threading.Thread(target=contador)
contador_thread.start()

# Inicia o loop assíncrono sem bloquear a thread principal
asyncio.run(main())

# Aguarda a thread do contador terminar
contador_thread.join()

print("Programa finalizado.")
