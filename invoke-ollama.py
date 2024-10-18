# coding: utf-8
from langchain_community.llms.ollama import Ollama
llm = Ollama(model="llama3.2:latest")
response = llm.invoke('What tree fits in your hand?')
print(response)
