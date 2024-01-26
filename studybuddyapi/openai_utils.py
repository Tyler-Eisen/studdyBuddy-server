import openai
import os

def generate_question(topic):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Create an interview question about: {topic}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def review_answer(answer):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # adjust the model as needed
        prompt=f"Review this answer for quality and relevance: {answer}",
        max_tokens=50
    )
    return response.choices[0].text.strip()
