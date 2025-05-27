import asyncio


async def diz_oi():
    print('Oi')
    await asyncio.sleep(2)
    print('Fim')

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(diz_oi())
event_loop.close()

# Bibliotecas Assíncronas
# https://github.com/aio-libs
# https://github.com/python/asyncio/wiki/ThirdParty
# https://pypi.org/search/?c=Framework+%3A%3A+AsyncIO
