from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq 
from prompt import SYSTEM_CHEF_PROMPT, CHEF_PROMPT
from langchain.messages import HumanMessage
from tools import web_search
from photo_decoder import choose_image_file, build_image_message
import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
load_dotenv()

logging.info("Creating out agent....")
model = ChatGroq(model = 'qwen/qwen3.8-27b')
agent = create_agent(model = model, system_prompt = SYSTEM_CHEF_PROMPT, tools=[web_search])

logging.info("Choosing our Image....")
path = choose_image_file()

message = build_image_message(path, CHEF_PROMPT)

logging.info("Invoking our agent....")
response = agent.invoke(
    {'messages': [message]}
    )
print(response['messages'][-1].content)

