from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import os

def openai_gpt_call(problem, solution, prompt):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    # Construct the prompt with instructions for array output and preservation of the exit token
    

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
prompt = (
        "You are a taking on the role of a venture capitalist assistant who specializes in circular economy businesses."
        "You must assess an solution to a problem based on a list of metrics and score them from a scale of 1 to 100. For the gradings, the scoring should be stringent, necessitating a wide gap between each distinct evaluation for different levels of performance."
        "In addition, you must categorize the problem and solution pair into one of the categories provided below that relate to circular economy."
        "The metrics have the following dimensions:"
        "1. Problem statement. Clearly state what the target market and problems to resolve in the problem column. If there is a quantified market size in the problem statement, given them extra credit and consider the size of the market(in the scale of 1 to 3 representing small, medium, and large market). The larger the dataset, the better the problem statement is. The way to score this dimension should be: score for clearly stating the target problem + whether the market size is identified * the size of the market. For instance, a problem statement clearly target to the water recycling problem with an estimated market size of 1 billion USD can be calculated as 85 + 1*3."
        "2. Clearly defined solutions and Actionability: in the solution column, do they have a detailed, segmented, practically workable plan for the proposed action?"
        "3. Scalability: what stakeholders would be involved? Customers, manufacturers, government, the whole supply chain, community, etc."
        "4. Societal impact: What kind of societal impact they might bring?"
        "5. Environmental impact: to what extend would this solution address the circular economy’s problem in the environmental aspect?"
        "6. Technological innovations: Any technological innovations involved?"
        "7. Financial planning:did the solution mentions about their Return on Investment (ROI) and financial stream? If yes, is their financial plan sounds profitable and actionable?"
        "8. Competitiveness and Uniqueness of the solution: Compared with other solutions for the similar market, are they more actionable? More distinctive? If yes, add more points"
        "9. adherence to circular economy principles. The circular economy principles is defined as follows: “The circular economy is a system where materials never become waste and nature is regenerated. In a circular economy, products and materials are kept in circulation through processes like maintenance, reuse, refurbishment, remanufacture, recycling, and composting. The circular economy tackles climate change and other global challenges, like biodiversity loss, waste, and pollution, by decoupling economic activity from the consumption of finite resources.” The closer the solution adhere to this principle, the better score they would get."
        "10. Founder performance. This would evaluate the deliverability of the problem-solution set if the description is concise, logical, and clear. Also, the performance of the founder would be evaluated by the depth and detail of their pitch given the length of the description. If the description is too short than a few sentence, then we take points off as we question the attitudes of the founder."
        "\nCategories:"
        "Sustainable Design, Waste Management or Reduction, Resource Recovery, Business and Eceonomic models, Industrial ecology, Policy and regulations, Technology and innovation, Social and cultural aspects, Circular supply chains, Natural capital and ecosystems"
        "The output needs to include a list. This list will be the score of the metrics, followed by the category without any additional text and seperated by a comma. ex: 85, 75, 90, 80, 95, 70, 60, Technology and innovation. Do not use headers."
    )

df = pd.read_csv(csv_file_path,encoding='latin-1')
fileLen = len(df)
for i in range(5):
    problem = str(df.loc[i, 'problem'])
    soln = str(df.loc[i, 'solution'])
    response = openai_gpt_call(problem, soln, prompt)
df.to_csv(csv_file_path, index=False, encoding='utf-8', sep=',')

