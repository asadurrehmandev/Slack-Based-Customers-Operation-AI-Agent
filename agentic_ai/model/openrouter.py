from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from configs import settings
from agentic_ai.tools.toolsets import *
from agentic_ai.tools.toolsets.dependencies import ToolDependencies

SYSTEM_PROMPT = """You are an AI assistant with access to external tools.

Whenever a user's request can be answered by a tool, you MUST call the appropriate tool.

Never claim that you cannot answer if an appropriate tool exists.
Never invent information.
Always use the provided tools first.
"""

model = OpenRouterModel(
    model_name=settings.LLM_MODEL_NAME,
    provider=OpenRouterProvider(
        api_key=settings.LLM_API_KEY,
    )
)

agent = Agent(
    model=model,
    toolsets=[
        communication_toolset,
        finance_toolset,
        weather_toolset,
    ],
    deps_type=ToolDependencies,
    system_prompt=SYSTEM_PROMPT,
)

if __name__ == "__main__":

    import asyncio

    async def main():

        from agentic_ai.providers.weather.weather import WeatherService, MockWeatherProvider
        from agentic_ai.providers.messenger.messenger import MessengerService, MessengerProviderFactory

        deps = ToolDependencies(
            weather_service=WeatherService(
                provider=MockWeatherProvider()
            ),
            messenger_service=MessengerService(
                factory=MessengerProviderFactory()
            )
        )

        results = await agent.run(
            "Notify asad about the weather in rawalpindi on whatsapp",
            deps=deps,
        )

        print(results.output)

    asyncio.run(main())