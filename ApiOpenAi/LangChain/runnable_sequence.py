import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')

prompt_template = PromptTemplate.from_template(
    'Me fale sobre o carro {carro}.'
)

runnable_sequence = prompt_template | model | StrOutputParser()

response = runnable_sequence.invoke({'carro': 'Marea 20v 1999'})

print(response)


runnable_sequence = (
    PromptTemplate.from_template(
        'Me fale sobre o carro {carro}.'
    )
    | model
    | StrOutputParser()
)

response = runnable_sequence.invoke({'carro': 'Marea 20v 1999'})

print(response)