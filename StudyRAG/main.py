from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI # type: ignore
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader # type: ignore

loader = PyPDFLoader("document/agenticai.pdf")
documents = loader.load()

model = ChatMistralAI(model_name="mistral-small-2506")
print("Done")