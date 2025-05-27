import asyncio
import time

async def gerar_dados(dados: asyncio.Queue):
    print('Gerando dados')
    for i in range(1000):
        await dados.put(i)
        await asyncio.sleep(0.001)
    print('Dados gerados')    

async def processar_dados(dados:asyncio.Queue):
    print('Processando dados')
    for i in range(1000):
        await dados.get()
        await asyncio.sleep(0.001)
    print('Dados processados')

async def main():
    dados = asyncio.Queue()
    
    inicio = time.time()
    
    tarefas = [
    gerar_dados(dados),
    gerar_dados(dados),
    processar_dados(dados),
    processar_dados(dados)
    ]
    
    await asyncio.gather(*tarefas)
    
    fim = time.time()
    print(f'Tempo: {fim - inicio}.')

asyncio.run(main())