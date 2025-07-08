from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

with open('questions.json', 'r') as f:
    questions = json.load(f)

    
plan_prompt = PromptTemplate(
    input_variables=["weak_topics"],
    template="""
You are a GMAT coach. Based on the following weak topics:
{weak_topics}
Generate a 1-week study plan focusing on improving these areas. Assign 1-2 topics per day.
"""
)
llm = OpenAI(temperature=0.2)

plan_chain = LLMChain(llm=llm, prompt=plan_prompt)

def generate_study_plan_with_llm(weak_topics):
    topic_str = ", ".join(topic for topic, _ in weak_topics)
    return plan_chain.run(weak_topics=topic_str)


def generate_study_plan_with_llm_indices(incorrect_indices):
    

# Example: map index to topic using your `questions` data


    weak_topics = [questions[i]["topic"] for i in incorrect_indices]
    unique_topics = list(set(weak_topics))
    topic_str = ", ".join(unique_topics)

    prompt_template = PromptTemplate(
        input_variables=["topics"],
        template=(
            "The student struggled with the following GMAT topics: {topics}.\n"
            "Create a very specific study plan focusing on these topics, with daily goals, tips, and resources in 500 words "
        )
    )

    study_plan_chain = LLMChain(llm=llm, prompt=prompt_template)
    response = study_plan_chain.run({"topics": topic_str})

    return response






                                             
