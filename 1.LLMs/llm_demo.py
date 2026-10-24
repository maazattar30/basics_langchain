from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=2,
    model_kwargs={"top_p":0.9}
)


response=llm.invoke("give me 5 names of muslim indian boys")
print(response.content)