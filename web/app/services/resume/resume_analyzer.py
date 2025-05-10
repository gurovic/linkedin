import requests
import json
import os

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')


def analyze_resume(text):
    """
    Отправляет текст резюме в DeepSeek API.
    Возвращает JSON с образованием, опытом работы и навыками.
    """
    prompt = f"""
You are an information extraction assistant. 
Given the following resume text, extract the following structured information:

1. Education: A list of universities the person studied at, with start_year and end_year.
2. Work Experience: A list of jobs with fields "company", "position", "start_year", "end_year".
3. Skills: A list of technical or professional skills.

Return strictly in JSON format like:
{{
  "education": [
    {{
      "university": "University Name",
      "start_year": 2015,
      "end_year": 2019
    }}
  ],
  "work_experience": [
    {{
      "company": "Company Name",
      "position": "Job Title",
      "start_year": 2020,
      "end_year": 2022
    }}
  ],
  "skills": ["Python", "Public Speaking"]
}}

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

        # 🔍 Печатаем реальный ответ, чтобы понять, что возвращает DeepSeek
        print("=== ОТВЕТ ОТ DEEPSEEK ===")
        print(response.text)

        data = response.json()

        # ✅ Подстраиваемся под разные форматы ошибок
        if "error" in data:
            return {"error": f"DeepSeek error: {data['error']}"}
        if "detail" in data:
            return {"error": f"DeepSeek says: {data['detail']}"}

        # ✅ Пытаемся получить нужный контент
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            return {"error": "Empty content from DeepSeek"}

        # ✅ Убираем Markdown-обёртку ```json ... ```
        if content.startswith("```json"):
            content = content.strip("` \n")  # удаляет ```json и ```
            content = content.replace("json", "", 1).strip()

        # ✅ Преобразуем текст в JSON
        return json.loads(content)

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {"error": "Failed to communicate with DeepSeek API"}

    except (KeyError, json.JSONDecodeError) as e:
        print(f"Response parsing error: {e}")
        return {"error": "Unexpected response format from DeepSeek"}