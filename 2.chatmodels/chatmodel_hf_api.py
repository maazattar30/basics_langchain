import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Use router.huggingface.co/v1 as the base_url
model = ChatOpenAI(
    model="meta-llama/Llama-3.1-8B-Instruct",
    api_key=hf_token,
    base_url="https://router.huggingface.co/v1",
)

result = model.invoke("what is MediaIQ Digital in India")
print(result.content)