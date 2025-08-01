# GMAT Quant - AI Tutor

An intelligent, interactive AI-powered tutor that helps GMAT aspirants master Quantitative topics with personalized insights and real-time question-answering, analysing their errors and rectifying thought processes for specific questions.

## Problem
GMAT aspirants face several challenges:

- No personalized feedback or tutoring.
- Overwhelming question banks with no smart guidance.
- Incomplete or unclear explanations.
- Fragmented practice with no performance tracking.
- No real-time support when stuck.

## Solution

**GMAT Quant - AI Tutor** addresses these pain points with:

-  **AI Tutor**: Analyses Users Steps and provides where they went wrong and the right step-by-step explanations.
-  **Smart Questioning**: Curated GMAT-style questions by topic & difficulty.
-  **Performance Analytics**: Tracks user progress and identifies weak areas.
-  **Personalized Practice**: Recommends questions based on user performance.


## Project Overview

**GMAT Quant - AI Tutor** is a web application designed to:
- Serve real GMAT-style quant questions across topics.
- Provide step-by-step explanations.
- Analyse test takers thought process for each question. 
- Analyze user performance.
- Recommend targeted practice.
- Use LLMs to act as a personalized AI tutor for learners.


##  Features

###  Core Capabilities
-  **Topic Coverage**: Number Properties, Word Problems, Geometry, Inequalities, Mixtures, etc.
-  **Difficulty Levels**: Easy, Medium, Hard
-  **AI Tutor**: Ask questions, get explanations, Analyse each step of user for every questions, and learn concepts interactively
-  **Performance Analytics**: Tracks accuracy, weak areas, and more
-  **Smart Practice Mode**: Recommends questions based on weaknesses

---

##  How It Works

1. **User selects a topic** (e.g., Probability)
2. **Question appears** with multiple-choice options
3. **Student Answers** with the necessary options and inputs the steps taken to reach the answer in the text box.
4. **Analysis of steps"" The steps are analysed and returned on what went right and wrong and how to approach in the right manner.
5. **AI Tutor provides hints or explanations** when prompted
6. **Backend logs the answer** and updates performance metrics
7. **Recommendations shown** after a short practice session


Built with:
-  **Backend**: Python
-  **Frontend**: streamlit
-  **AI Engine**: OpenAI (via LangChain)
-  **Data**: Scraped GMAT Club questions, cleaned and structured as JSON

---
# Overview 
<img width="1014" height="916" alt="gmat_tutor" src="https://github.com/user-attachments/assets/453434c7-decf-44d3-8744-de71d3f7154d" />


## Question-Bank Data Format (Example)

```json
{
  "question_id": "Q1234",
  "topic": "Probability",
  "difficulty": "Medium",
  "question": "If two dice are rolled, what is the probability that the sum is 7?",
  "options": {
    "A": "1/6",
    "B": "1/12",
    "C": "1/36",
    "D": "5/36",
    "E": "1/2"
  },
  "correct_answer": "A",
  "explanation": "There are 6 combinations that add up to 7: (1,6), (2,5), ..., (6,1). Total possible outcomes = 36. So, 6/36 = 1/6."
}
```
---
## Future Iterations

- Make Real-time Adaptive test similar to GMAT Testing
- Refined UI with Question Banks and learning resources for each Topics
- Overall Error Logging and AI Analysis to Analyse Users Patterns
- Seamless Setup and Daily Test-Taking Question Bank that matches the Users Lifestyle.
