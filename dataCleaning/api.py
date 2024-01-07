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
    messages = [
    {
        "role": "system",
        "content": (
            "You are a data cleaner. The user will input an environmental or business problem, and the user will input a solution using circular economy principles. These are seperated by a newline character"
            "This data is not cleaned. You act as a data cleaner who will remove all punctuation, grammar, and spelling errors. This does not include the unique character sequence #@#"
            "You will also make the data concise and easy to understand. The objective is to prepare the data for another language model that will be trained on this cleaned data. "
            "Ensure the result is not longer than the original prompt. Check to ensure you have not deleted #@# from the original prompt. If you have, put them back."
        ),
    },
    {"role": "user", "content": f"{problem}#@#{solution}"},
    ]

    )
    responseString = completion.choices[0].message.content
    print(responseString)
    response = responseString.split("#@#")
    print(response[0])
    print(response[1])
    return response

load_dotenv()
csv_file_path = os.getenv("CSV_FILE_PATH")
df = pd.read_csv(csv_file_path,encoding='latin-1')
fileLen = len(df)
for i in range(5):
    problem = str(df.loc[i, 'problem'])
    soln = str(df.loc[i, 'solution'])
    print(f"{problem}\n{soln}")
    #response = openAIGPTcall(problem, soln)
df.to_csv(csv_file_path, index=False, encoding='utf-8', sep=',')
print(f"File '{csv_file_path}' has been updated.")

