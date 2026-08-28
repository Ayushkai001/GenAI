from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI # type: ignore
load_dotenv()

model = ChatMistralAI(model_name="mistral-small-2506")