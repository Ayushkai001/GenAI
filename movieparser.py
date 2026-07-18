from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_mistralai import ChatMistralAI # type: ignore
from langchain_core.output_parsers import PydanticOutputParser # type: ignore
from pydantic import BaseModel
from typing import List, Optional

#Creating a Schema for the movie data using Pydantic's BaseModel
class Movie(BaseModel):
    title: str
    director: str
    release_year: int
    genre: List[str]
    cast: List[str]
    rating: Optional[float] = None
    summary: Optional[str] = None 

parser = PydanticOutputParser(pydantic_object=Movie)

model = ChatMistralAI(model = "mistral-small-latest") 

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert movie data extraction assistant.
                {format_instructions}"""),
    ("human", "{paragraph}")
])

para = input("Enter the paragraph containing movie information : ")

final_prompt = prompt.invoke(
    {
        "paragraph": para,
        "format_instructions": parser.get_format_instructions()
    }
)
response = model.invoke(final_prompt)
movie_data = parser.parse(response.content)
 
print ('\nExtracted Movie Data : \n' , movie_data)



#To Test the code, you can use the following paragraph as input:
#Widely regarded as one of Christopher Nolan's finest works, Interstellar was released in 2014 and blends Science Fiction, Adventure, and Drama into an emotional story about humanity's survival. The film follows former NASA pilot Cooper, played by Matthew McConaughey, who joins a mission through a mysterious wormhole alongside Anne Hathaway and a talented cast including Jessica Chastain, Michael Caine, and Matt Damon. Praised for its scientific accuracy, breathtaking visuals, and Hans Zimmer's unforgettable score, the movie has earned an IMDb rating of 8.7 and continues to be celebrated as one of the greatest science fiction films ever made.