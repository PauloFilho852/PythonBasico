import os
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import dotenv

dotenv.load_dotenv()

model = ChatOpenAI(
    model='gpt-4',
)

persist_directory = 'db'
embedding = OpenAIEmbeddings()

vector_store = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding,
    collection_name='laptop_manual',
)

retriever = vector_store.as_retriever()

system_prompt = '''
Você é um assistente muito últil. O usuário entrará com questões que deverão ser respondidas conforme o contexto obtido de um banco de dados vetorial.
'''
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('human', 'Questão: {input}. Contexto: {context}'),
    ]
)
question_answer_chain = create_stuff_documents_chain(
    llm=model,
    prompt=prompt
)
chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=question_answer_chain,
)

query = 'Qual a marca e o modelo do notebook?'

response = chain.invoke(
    {'input': query},
)

print(response['answer'])
