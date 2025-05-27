import asyncio
import aiofiles
import aiohttp
import bs4


async def pegar_links():
    links = []
    async with aiofiles.open('links.txt') as arquivo:
        async for link in arquivo:
            links.append(link.strip())
    return links


async def pegar_html(link):
    print(f'Pegando o HTML do curso {link}')

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            try:
                resp.raise_for_status()
                return await resp.text()
            except Exception as e:
                print(f'Erro na requisição {e}')


def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title')
    title = title.text
    return title


async def main():
    links = await pegar_links()
    corrotinas = [pegar_html(link) for link in links]
    htmls = await asyncio.gather(*corrotinas)

    for html in htmls:
        title = pegar_titulo(html)
        print(f'Title: {title}')


asyncio.run(main())
