from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1
)


response=llm.invoke("what is capital of india")
print(response)