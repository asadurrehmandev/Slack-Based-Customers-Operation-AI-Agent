from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from core.configs import settings

DEEPSEEK_v4_FLASH = OpenRouterModel(
    model_name="~deepseek/deepseek-v4-flash-latest",
    provider=OpenRouterProvider(
        api_key=settings.LLM_API_KEY,
    )
)
