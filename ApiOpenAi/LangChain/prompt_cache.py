import os
from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

model = OpenAI()

# Mantém respostas em cache na memória, para responder a perguntas repetidas
# set_llm_cache(InMemoryCache())

# Persisite respostas, para responder perguntas repetidas
set_llm_cache(SQLiteCache(database_path='openai_cache.db'))

prompt = 'Me diga quem foi Alan Turing.'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2}')
