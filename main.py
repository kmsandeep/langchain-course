import os
from http.client import responses

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


def main():
    load_dotenv()

    # llm = ChatGoogleGenerativeAI(
    #     model="gemini-2.5-flash",
    #     temperature=0.3
    # )

    llm = ChatOllama(
        model="gemma3:270m",
        temperature=0.3
    )

    article_content = """
    Generative AI is transforming the landscape of software engineering by automating repetitive coding tasks. 
    Tools like GitHub Copilot and Gemini are now integrated directly into IDEs, allowing developers to generate 
    boilerplate code, debug complex algorithms, and even write unit tests. While some fear the displacement 
    of human roles, most experts agree that AI acts as a 'force multiplier,' enabling engineers to focus 
    on high-level system architecture and problem-solving rather than syntax.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an expert editorial assistant. Your task is to provide a concise, professional summary of the provided text."),
        ("human",
         "Please summarize the following article into {word_count} words or less, focusing on the core thesis and key takeaways:\n\n{article_text}")
    ])
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(input={
        "article_text": article_content,
        "word_count": "50"
    })
    print("Summary:", response)


if __name__ == "__main__":
    main()
