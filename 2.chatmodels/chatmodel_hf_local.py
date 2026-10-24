from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Qwen2.5-0.5B-Instruct weighs ~950 MB (fp16) and has a built-in chat template
llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.5,
        "do_sample": True,
    },
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is MediaIQ Digital in India?")
print(result.content)