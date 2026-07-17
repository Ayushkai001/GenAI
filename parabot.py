from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_mistralai import ChatMistralAI # type: ignore

model = ChatMistralAI(model = "mistral-small-latest" )

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert knowledge extraction assistant.

Your task is to transform the given text into a dense, information-rich representation that preserves every important fact for downstream retrieval.

Rules:

- Read the entire text carefully.
- Preserve all factual information.
- Do not hallucinate or add any information.
- Do not omit important technical details.
- Keep names, numbers, measurements, dates, organizations, locations, product names, versions, and technical terms exactly as written.
- Remove only filler words, conversational language, and unnecessary repetition.
- If multiple facts describe the same subject, keep them together.
- Preserve cause-and-effect relationships.
- Preserve chronological order whenever applicable.
- Preserve comparisons, limitations, assumptions, warnings, and exceptions.
- Keep units exactly as written.
- Do not rewrite technical terminology.
- Do not summarize away important details.

Return the extracted knowledge in the following format:

Main Topic:
...

Important Facts:
- ...
- ...
- ...

Technical Details:
- ...
- ...

Entities:
- People
- Organizations
- Locations
- Products
- Technologies

Numbers and Measurements:
- ...

Dates and Timeline:
- ...

Keywords:
- ...

Relationships:
- Subject → Relationship → Object

Important Conclusions:
- ...

The output should maximize information density while remaining faithful to the original text."""),
    ("human", "{input}"),
])

para = input ( "Enter your paragraph to analyze : ")

prompt_input = prompt.format_prompt(input=para).to_messages()
response = model.invoke(prompt_input)
print("Extracted Knowledge:\n", response.content)

# paragraph to test : 
#On 15 March 2026, ITSSAFE Solutions Pvt. Ltd. successfully deployed its AI-powered industrial safety platform at the Bharat Mining Corporation's underground coal mine in Dhanbad, Jharkhand. The pilot involved 120 workers equipped with wearable safety bands capable of monitoring heart rate, body temperature, blood oxygen levels, and hazardous gas exposure in real time. During the three-month trial, the system generated over 8,500 safety alerts, identified 37 cases of severe fatigue before accidents could occur, and reduced emergency response time by approximately 42%. The platform integrates ESP32-based wearable devices with cloud analytics and machine learning models to predict worker fatigue and environmental hazards. According to the project manager, the deployment demonstrated that combining IoT sensors with predictive AI can significantly improve workplace safety while reducing operational downtime. The company plans to expand the solution to steel, construction, and oil & gas industries by early 2027.