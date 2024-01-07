from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import os

def openai_gpt_call(problem, solution):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Construct the prompt with instructions for array output and preservation of the exit token
    prompt = (
        "You are a taking on the role of a venture capitalist assistant who specializes in circular economy businesses. You must assess an solution to a problem based on a list of metrics and score them from a scale of 1 to 100"
        "The metrics are the following: Unique Value Proposition (UVP), Actionability, Scalability: what stakeholders would be involved?, Innovation: How technologically innovative is it, Return on Investment and financial stream, Competitiveness, Adherence to circular economy principles"
        "The output needs to include a list. This list will be the score of the metrics, without any additional text and seperated by a comma. ex: 85, 75, 90, 80, 95, 70, 60. Do not use headers."
    )

    # Make the API call
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Problem: {problem}\nSolution: {solution}"},
        ],
        temperature=0.2
    )

    
    # Extract the generated text from the API response
    generated_text = completion.choices[0].message.content
    # Split the response into an array using the exit token
    response_array = generated_text.split(", ")
    print(response_array)
    return response_array

load_dotenv()
csv_file_path = os.getenv("CSV_FILE_PATH")
df = pd.read_csv(csv_file_path,encoding='latin-1')
fileLen = len(df)
for i in range(5):
    problem = str(df.loc[i, 'problem'])
    soln = str(df.loc[i, 'solution'])
    response = openai_gpt_call(problem, soln)
df.to_csv(csv_file_path, index=False, encoding='utf-8', sep=',')

