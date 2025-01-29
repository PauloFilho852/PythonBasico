
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
import dotenv

dotenv.load_dotenv()

model = ChatOpenAI(
    model='gpt-4o',
)

persist_directory = 'db'
embedding = OpenAIEmbeddings()

vector_store = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding,
    collection_name='laptop_manual',
)

retriever = vector_store.as_retriever()

question = "Como posso falar com a assistência técnica?"

result = retriever.invoke(question)

context = ''
for res in result:
    context = context + res.page_content


system_prompt = '''
Você é um assistente muito últil. O usuário entrará com questões que deverão ser respondidas conforme o contexto obtido de um banco de dados vetorial.
'''
chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('human', 'Questão: {question}. Contexto: {context}'),
    ]
)

rag_chain = (
    chat_template
    | model
    | StrOutputParser()
)

response = rag_chain.invoke({'question': question, 'context': context})

print(response)
