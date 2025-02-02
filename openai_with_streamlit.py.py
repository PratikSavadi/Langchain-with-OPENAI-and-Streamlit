from langchain_openai import  ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['PROJECT']=os.getenv('LANGCHAIN_PROJECT')


prompt=ChatPromptTemplate.from_messages(
    [
        ('system','you are helpful assistant. Please response to the user quires'),
        ('user','Question:{question}')
    ]
)

st.title('LangChain Demo with OpenAI')
input_text=st.text_input('Search the topic u want')

llm=ChatOpenAI(model='gpt-3.5-turbo-0125')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

