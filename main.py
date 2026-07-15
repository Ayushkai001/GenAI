from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-latest" ) 

prompt = input("Enter your prompt: ")

response = model.invoke(prompt)
print("Response:", response.content)
