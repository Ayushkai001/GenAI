from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI # type: ignore
load_dotenv()

mistral = ChatMistralAI.from_env()