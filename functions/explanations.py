from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Choose LLM — or use HuggingFaceHub or OpenRouter
llm = OpenAI(temperature=0.2)

# Create template
template = """
You are an expert GMAT math tutor. For each question, provide the correct answer and explain your reasoning step-by-step, with each step on a new line.

---

Question 1:
What is the remainder when 49 is divided by 6?

Correct Answer: 1

Explanation:
1. Divide 49 by 6: 49 ÷ 6 = 8 with a remainder.
2. 6 × 8 = 48.
3. 49 - 48 = 1.
→ The remainder is 1.

---

Question 2:
If x is an even integer, which of the following must be true?
A. x is divisible by 2  
B. x + 1 is even  
C. x - 1 is divisible by 2

Correct Answer: A

Explanation:
1. By definition, an even number is divisible by 2.
2. x + 1 is odd (since even + 1 = odd), so B is false.
3. x - 1 is also odd, so it is not divisible by 2.
→ Only A must be true.

---

Question 3:
{question}

Correct Answer: {answer}

Explanation:
"""

prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template=template,
)



template_user_steps = """
You are a GMAT tutor.

Question:
{question}

Correct Answer:
{answer}

User's Reasoning:
{user_steps}

Please check the reasoning against the correct logic and explain:
- Where the user made mistakes (if any)
- What they misunderstood
- A clear, minimal suggestion to improve
"""

prompt_user_steps = PromptTemplate(
    input_variables=["question", "answer", "user_steps" ],
    template=template_user_steps,
)


explanation_user_steps_chain = LLMChain(llm=llm, prompt=prompt_user_steps)
# Create chain
explanation_chain = LLMChain(llm=llm, prompt=prompt)

# Use this function in your Streamlit app
def get_llm_explanation(question, answer):
    return explanation_chain.run(question=question, answer=answer)

def get_llm_explanation_with_user_steps( question, answer, user_steps):
    explanation_user_str = explanation_user_steps_chain.invoke({"question": question, "answer": answer, "user_steps": user_steps})
    result = explanation_user_str['text']
    return result 