from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables
import os
import pandas as pd
import google.generativeai as genai
## Configure Genai Key
import time
from tqdm import tqdm
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(prompt):
    model=genai.GenerativeModel('gemini-pro', generation_config = {
        "temperature": 0,
    })
    response=model.generate_content([prompt],safety_settings=safety_settings)
    return response.text
df = pd.read_csv('your csv file path')
df = df[6921:]

for index, row in tqdm(df.iterrows(), total=len(df)):
    # merged = row['merged']
    heading = row['Heading']
    description = row['Description']

    # Example: Print values or perform operations
    prompt = f"""You are an expert at making questions and answers from the given text description.
    I will provide you with the heading and corresponding description of Bangladeshi law data.
    Now your task is to make at least 3 questions and corresponding answers from the given Bangla text law data in bangla languages. and the question will generate in a such way is related to heading 


    heading: {heading}
    description: {description}
    """
    response = get_gemini_response(prompt)
    
    file_path = os.path.join('output', f'response_{index}.txt')
    with open(file_path, 'w') as f:
        f.write(response)
    









