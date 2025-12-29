from langchain_core.prompts import ChatPromptTemplate
from helper.prompt import system_prompt


def get_prompt_template():
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("user", "{question}")]
    )

    return prompt_template
