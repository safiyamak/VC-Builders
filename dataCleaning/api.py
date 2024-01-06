from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import os

def openAIGPTcall(problem, solution):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a data cleaner. The user will input an environmental or business problem and the user will input a solution using circular economy principles. This data is not cleaned. You act as a data cleaner who will remove all punctuation, grammar, and spelling errors. You will also make the data concise and easy to understand for another LLM that will be trained on this data."},
        {"role": "user", "content": "Problem: " + problem + "; solution: " + solution}
    ]
    )
    print(completion.choices[0].message)


