import asyncio
import time


async def tarefa(nome, tempo):
    print(f"{nome} iniciada. Vai demorar {tempo}s...")
    await asyncio.sleep(tempo)
    print(f"{nome} concluída.")
    return nome, tempo


async def main():
    print("Main iniciada")
    tarefas = [
        tarefa("Tarefa 1", 2),
        tarefa("Tarefa 2", 3)
    ]
    for coro in asyncio.as_completed(tarefas):
        resultado = await coro
        print(f"Resultado recebido: {resultado}")
    print("Main concluída")

print("Início do programa")
start = time.time()
asyncio.run(main())
print("Fim do programa")
print(f"Tempo total: {time.time() - start:.2f}s")
