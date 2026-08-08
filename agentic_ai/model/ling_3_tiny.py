from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from core.configs import settings

LING_3_TINY = OpenRouterModel(
    model_name="inclusionai/ling-3.0-tiny:free",
    provider=OpenRouterProvider(
        api_key=settings.LLM_API_KEY,
    )
)
