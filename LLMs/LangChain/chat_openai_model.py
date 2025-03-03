import os
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

"""
model = OpenAI()

response = model.invoke(
    input='Quem foi Alan Turing?',
    temperature=1,
    max_tokens=500,
)

print(response)
"""

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=1,
    max_tokens=100
)

messages = [
    {'role': 'system', 'content': 'Você é um assistente que fornece informações sobre figuras históricas.'},
    {'role': 'user', 'content': 'Quem foi Alan Turing?'}
]

response = model.invoke(messages)

# print(response)
print(response.content)
