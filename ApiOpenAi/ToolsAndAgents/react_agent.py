import os
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')

prompt = '''
Como assistente financeiro pessoal, que responderá as perguntas dando dicas financeiras e de investimentos.
Responda tudo em português brasileiro.
Perguntas: {q}
'''
prompt_template = PromptTemplate.from_template(prompt)

python_repl = PythonREPL()
python_repl_tool = Tool(
    name='Python REPL',
    description='Um shell Python. Use isso para executar código Python. Execute apenas códigos Python válidos.'
                'Se você precisar obter o retorno do código, use a função "print(...)".'
                'Use para realizar cálculos financeiros necessários para responder as perguntas e dar dicas.',
    func=python_repl.run
)

search = DuckDuckGoSearchRun()
duckduckgo_tool = Tool(
    name='Busca DuckDuckGo',
    description='Útil para encontrar informações e dicas de economia e opções de investimento.'
                'Você sempre deve pesquisar na internet as melhores dicas usando esta ferramenta, não'
                'responda diretamente. Sua resposta deve informar que há elementos pesquisados na internet.',
    func=search.run,
)

react_instructions = hub.pull('hwchase17/react')

tools = [python_repl_tool, duckduckgo_tool]

react_agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=react_instructions,
)

agent_executor = AgentExecutor(
    agent=react_agent,
    tools=tools,
    verbose=True,
)

question = ''''
Minha renda é de R$10000 por mês, tenho muitas faturas de cartões de crédito num total de R$12000 por mês.
Tenho mais despesas de aluguel e combustível, num total R$ 1500.
Quais dicas você pode me dá?
'''

output = agent_executor.invoke(
    {'input': prompt_template.format(q=question)}
)

print(output.get('output'))
