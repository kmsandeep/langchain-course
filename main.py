from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavilyClient = TavilyClient()
@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: search query
    Returns:
        search results
    """
    print(f"Searching for: {query}")
    return tavilyClient.search(query=query)


def main():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )
    # llm = ChatOllama(
    #     model="gemma3:270m",
    #     temperature=0.3
    # )
    agent = create_agent(llm, tools=[TavilySearch()])
    response = agent.invoke({"messages": HumanMessage("What is the weather in Tokio?")})
    print(response)


if __name__ == "__main__":
    main()
