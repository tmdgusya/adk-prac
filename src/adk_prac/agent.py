import os
import urllib.parse
import json
import httpx
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


# Ollama 모델 설정 - 사용하려는 모델명으로 변경
OLLAMA_MODEL = "ollama_chat/qwen3:4b"

async def search_naver_blog(query: str) -> str:
    """네이버 블로그에서 정보를 검색합니다."""
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")

    if not client_id or not client_secret:
        return "Error: NAVER_CLIENT_ID or NAVER_CLIENT_SECRET not found."

    try:
        encText = urllib.parse.quote(query)
        url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText + "&display=5"
        headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            results = []
            for item in items:
                title = item['title'].replace("<b>", "").replace("</b>", "")
                description = item['description'].replace("<b>", "").replace("</b>", "")
                results.append({
                    "title": title,
                    "link": item['link'],
                    "description": description
                })
            return json.dumps(results, ensure_ascii=False, indent=2)
        else:
            return f"Error Code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# 간단한 도구 예시
def get_weather(city: str) -> str:
    """도시의 날씨를 반환합니다."""
    weather_data = {
        "seoul": "서울: 맑음, 22°C",
        "tokyo": "도쿄: 흐림, 18°C",
        "new york": "뉴욕: 비, 15°C",
    }
    return weather_data.get(city.lower(), f"{city}: 정보를 찾을 수 없습니다.")


def calculate(a: int, b: int, operation: str) -> str:
    """간단한 계산을 수행합니다."""
    if operation == "add":
        return f"{a} + {b} = {a + b}"
    elif operation == "subtract":
        return f"{a} - {b} = {a - b}"
    elif operation == "multiply":
        return f"{a} * {b} = {a * b}"
    elif operation == "divide":
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return f"{a} / {b} = {a / b}"
    else:
        return f"알 수 없는 연산: {operation}"


# ADK Agent 정의
# ADK looks for an 'agent' or similar object. Renaming root_agent to agent for clarity/convention.
root_agent = Agent(
    model=LiteLlm(model=OLLAMA_MODEL),
    name="ollama_assistant",
    description="Ollama 모델을 사용하는 AI 어시스턴트",
    instruction="""당신은 도움이 되는 어시스턴트입니다.
사용자의 질문에 답하고, 날씨 정보를 제공하며, 계산을 도와줄 수 있습니다.
또한 네이버 블로그 검색을 통해 최신 정보를 찾아볼 수 있습니다.
도구를 사용할 때는 반드시 JSON 형식으로 응답하세요.""",
    tools=[get_weather, calculate, search_naver_blog],
)
