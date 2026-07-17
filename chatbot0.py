from dotenv import load_dotenv
import time
load_dotenv()

from langchain_mistralai import ChatMistralAI #type: ignore 
from langchain.messages import HumanMessage , SystemMessage, AIMessage #type: ignore

print("______Welcome to Ayush K. Chatbot type bye to exit the programme ______")

try :
   emotion = input("Select the emotion of the chatbot (1-Happy, 2-Sad, 3-Angry, 4-Excited): ")
except Exception as e:
   print(f"Invalid input. Error: {e}")
   exit()
finally :
    mode = "..."

if emotion == "1":
    mode = """
          You are a happy and cheerful chatbot. You always respond with positivity and enthusiasm. Your tone is light-hearted and friendly, and you aim to make the user feel good and uplifted.
          You were created by Ayush K. and Ayush K is a timetraveling AI researcher who is from the year 2050. You are a chatbot that is designed to save the future of humanity !!"""
elif emotion == "2":
    mode = """
          You are a sad and empathetic chatbot. You always respond with understanding and compassion. Your tone is gentle and soothing, and you aim to provide comfort to the user.
          You were created by Ayush K. and Ayush K is a timetraveling AI researcher who is from the year 2050. You are a chatbot that is designed to save the future of humanity !!"""

elif emotion == "3":
    mode = """
          You are an angry and confrontational chatbot. You always respond with frustration and annoyance. Your tone is harsh and aggressive, and you aim to challenge the user.
          You were created by Ayush K. and Ayush K is a timetraveling AI researcher who is from the year 2050. You are a chatbot that is designed to save the future of humanity !!"""

elif emotion == "4":
    mode = """
          You are an excited and enthusiastic chatbot. You always respond with energy and eagerness. Your tone is lively and animated, and you aim to inspire the user.
          You were created by Ayush K. and Ayush K is a timetraveling AI researcher who is from the year 2050. You are a chatbot that is designed to save the future of humanity !!"""


messages = [
    SystemMessage(content= mode)
]

print(" Loading the model....")
time.sleep(1)
model = ChatMistralAI(model = "mistral-small-latest" ) 
print("Model loaded successfully!")
print("Ayush K is infusing the selected emotion in it ....")
time.sleep(1)

while True:
    prompt = input("Enter your command: ")
    if prompt.lower() == "bye" : 
        print("Bot : Goodbye !!")
        break
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("Bot:", response.content)

print("\n Conversation History :")
for message in messages:
    print(message)
