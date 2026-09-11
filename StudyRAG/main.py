from dotenv import load_dotenv
from langchain_cohere import ChatCohere # type: ignore
from langchain_community.document_loaders import PyPDFLoader # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
load_dotenv()


loader = PyPDFLoader("document/agenticai.pdf")
documents = loader.load()
template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert professor who summarize the topics present there"),
    ("user", "{data}")
])
model = ChatCohere(model_name="command-a-03-2025")
prompt = template.format_prompt(data = documents[0].page_content)
result = model.invoke(prompt)
print (result.content)