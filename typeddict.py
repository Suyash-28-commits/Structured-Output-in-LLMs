from langchain_openai import ChatOpenAI
from typing import TypedDict , Annotated, Optional , Literal
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
    model ="allenai/olmo-3.1-32b-think:free",
    openai_api_key = OPENROUTER_API_KEY,
    openai_api_base= OPENROUTER_API_BASE
)
#Problem statement : I have review of a product and I have to generate summary and sentiment of it 
#The ouput should be structured 

#Using TypedDict Class to strutcure review and it's sentiment for getting structured output
class Review(TypedDict):
    key_themes : Annotated[list[str],"Write down the key themes discussed in the review in a list"]
    summary : Annotated[str,"Give a brief summary"] #Annotated definition for llm
    sentiment : Annotated[Literal["pos","neg"],"Give sentiment of the review with either positive,negative or neutral"]
    pros : Annotated[Optional[list[str]],"Write all the pros in the review in the form of a list"]
    cons : Annotated[Optional[list[str]],"Write all the cons in the review in the form of a list"]
    name : Annotated[Optional[str],"Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)
# result = structured_model.invoke("""The hardware is great , but the software feels bloated . There are too many pre installed apps that I can't remove .Also the UI looks outdated compared to other brands.Hoping for a software update to fix this""")
result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:

Insanely powerful processor (great for gaming and productivity)

Stunning 200MP camera with incredible zoom capabilities

Long battery life with fast charging

S-Pen support is unique and useful

Cons:

Bulky and heavy-not great for one-handed use

Bloatware still exists in One UI

Expensive compared to competitors 
""")
print(result)
print("\n")
print("\n")
# print(result['pros'])
# print(result['cons'])
# print(result['summary'])
# print(result['sentiment'])
print(result.keys())
#Composition of a typped dictionary
class Review1(TypedDict):
    key_themes : str
    name : str
    sentiment : str
    pros : Annotated[Optional[list[str]],"Write pros of a review in list"]
    cons : Annotated[Optional[list[str]],"Write cons of a review in list"]

review1 : Review1 = {}