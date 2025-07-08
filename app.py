import streamlit as st
import json
from functions.performance_tracker import update_performance, analyze_weaknesses
from functions.study_plan import generate_study_plan_with_llm_indices
from functions.explanations import get_llm_explanation, get_llm_explanation_with_user_steps

from dotenv import load_dotenv
import os
import time

from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache

set_llm_cache(InMemoryCache())

load_dotenv()  
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load questions from JSON file
with open('questions.json', 'r') as f:
    
    questions = json.load(f)
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "explanations" not in st.session_state:
    st.session_state.explanations = {}

q_idx = st.session_state.question_index
q_data = questions[q_idx]

st.title(" GMAT AI Tutor – Practice Test")
st.subheader(f"Question {q_idx + 1} of {len(questions)}")
st.markdown(f"**{q_data['question']}**") 

# Answer input 
user_input = st.radio("Choose your answer:", q_data["options"], key=f"radio_{q_idx}")
user_steps = st.text_area("Explain your steps to reach this answer (optional):", key=f"steps_{q_idx}")


# Submit logic 
if st.button("Submit") and not st.session_state.submitted:
    correct = user_input.strip().lower() == q_data["answer"].strip().lower()
    st.session_state.answers[q_idx] = {
        "question": q_data["question"],
        "user_answer": user_input,
        "correct_answer": q_data["answer"],
        "is_correct": correct,
        "user_steps": user_steps
    }

    explanation = get_llm_explanation( q_data["question"], user_input)
    user_response = get_llm_explanation_with_user_steps(q_data["question"], user_input, user_steps)
    st.session_state.explanations[q_idx] = explanation

    if correct:
        st.success("Your answer is correct!")
    else:
        st.error("Your answer is incorrect.")

    st.markdown(f"**Correct Answer:** {q_data['answer']}")
    st.markdown(f"**Your Answer:** {user_input}")
    st.markdown(f"### Explanation:\n{explanation}")
    st.markdown(f"### Analysis :\n{user_response}")
    st.session_state.submitted = True  # 🔹 Mark as submitted


#  NEXT BUTTON appears only after submission 
if st.session_state.submitted and q_idx < len(questions) - 1:
    if st.button("Next"):
        st.session_state.submitted = False
        st.session_state.question_index += 1
        st.rerun()


#  Show results after final question
if q_idx == len(questions) - 1 and len(st.session_state.answers) == len(questions):
    st.markdown("---")
    st.header("Your Performance Summary")

    correct_count = sum([1 for v in st.session_state.answers.values() if v["is_correct"]])
    incorrect_indices = [i for i, v in st.session_state.answers.items() if not v["is_correct"]]

    st.write(f"**Total Score:** {correct_count} / {len(questions)}")

    if incorrect_indices:
        st.subheader(" Weak Areas Identified")
        for idx in incorrect_indices:
            st.write(f"- Q{idx+1}: {questions[idx]['question']}")

        if st.button("Generate Study Plan"):
            plan = generate_study_plan_with_llm_indices(incorrect_indices)
            st.markdown("###  Personalized Study Plan")
            st.markdown(plan)
    else:
        st.success(" Excellent! You got everything right.")
