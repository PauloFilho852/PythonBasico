import asyncio
import time


async def tarefa(nome, tempo):
    print(f"{nome} iniciada. Vai demorar {tempo}s...")
    await asyncio.sleep(tempo)
    print(f"{nome} concluída.")
    return tempo


async def main():
    print("Main iniciada")
    resultado1 = await tarefa("Tarefa 1", 2)
    resultado2 = await tarefa("Tarefa 2", 3)
    print(f"Resultados: {resultado1}, {resultado2}")
    print("Main concluída")

print("Início do programa")
start = time.time()
asyncio.run(main())
print("Fim do programa")
print(f"Tempo total: {time.time() - start:.2f}s")
