import requests
import json
import os

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')

def analyze_resume(text):
    """
    Sends resume text to DeepSeek API and retrieves university education details.
    Returns a list of dictionaries like:
    [
        {
            "university": "Harvard University",
            "start_year": 2015,
            "end_year": 2019
        },
        ...
    ]
    """
    prompt = f"""
You are an information extraction assistant. 
Given the following resume text, extract a list of universities where the person studied, along with start_year and end_year of study.

Return the data strictly in JSON format like:
[
  {{
    "university": "University Name",
    "start_year": 2015,
    "end_year": 2019
  }},
  ...
]

Only return the JSON. Do not include any extra text.

Resume text:
\"\"\"
{text}
\"\"\"
"""

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a resume parsing assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]

        result = json.loads(content)
        return result

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {"error": "Failed to communicate with DeepSeek API"}

    except (KeyError, json.JSONDecodeError) as e:
        print(f"Response parsing error: {e}")
        return {"error": "Unexpected response format from DeepSeek"}
