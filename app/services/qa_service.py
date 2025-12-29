from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from helper.qa_helper import get_prompt_template
from core.config import settings


model = ChatGroq(model=settings.default_model, api_key=settings.groq_api)


def generate_answer(character: str, context: str, question: str) -> str:
    chain = get_prompt_template() | model | StrOutputParser()
    llm_prompt = {
        "character": character,
        "context": context,
        "question": question,
    }

    answer = chain.invoke(llm_prompt)
    return answer
