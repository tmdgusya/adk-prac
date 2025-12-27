import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Ollama 모델 설정 - 사용하려는 모델명으로 변경
# 권장: ollama_chat provider (올바른 도구 처리와 컨텍스트 관리)
OLLAMA_MODEL = "ollama_chat/qwen3:4b"

# 또는 OpenAI 호환 endpoint 사용:
# OLLAMA_MODEL = "openai/llama3.2"

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
root_agent = Agent(
    model=LiteLlm(model=OLLAMA_MODEL),
    name="ollama_assistant",
    description="Ollama 모델을 사용하는 AI 어시스턴트",
    instruction="""당신은 도움이 되는 어시스턴트입니다.
사용자의 질문에 답하고, 날씨 정보를 제공하며, 계산을 도와줄 수 있습니다.
도구를 사용할 때는 반드시 JSON 형식으로 응답하세요.""",
    tools=[get_weather, calculate],
)


def main():
    """CLI 모드에서 에이전트 테스트"""
    print("=" * 50)
    print("Google ADK + Ollama 연동 예제")
    print("=" * 50)
    print(f"사용 모델: {OLLAMA_MODEL}")
    print()
    print("사용 가능한 도구:")
    print("  - get_weather: 도시 날씨 조회")
    print("  - calculate: 간단한 계산")
    print()
    print("tip: 'adk web' 명령어로 웹 UI를 실행할 수 있습니다.")
    print("     또는 ADK 웹 서버를 통해 대화를 테스트하세요.")


if __name__ == "__main__":
    main()
