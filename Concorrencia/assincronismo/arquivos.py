import aiofiles
import asyncio

import aiofiles


async def exemplo1():
    async with aiofiles.open("texto.txt") as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo2():
    async with aiofiles.open('texto.txt') as arquivo:
        async for linha in arquivo:
            print(linha)


async def main():
    # await exemplo1()
    await exemplo2()


asyncio.run(main())
