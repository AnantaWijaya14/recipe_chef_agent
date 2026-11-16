from dotenv import load_dotenv
from langchain.tools import tool
from tavily import  TavilyClient
from typing import Dict, Any
import logging 

load_dotenv()

travily_client = TavilyClient()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

@tool
def web_search(query:str)->Dict[str, Any]:
    """tool to search the web for information  """
    logging.info(f'Searching for {query}')
    return travily_client.search(query)