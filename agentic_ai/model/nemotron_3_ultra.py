from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from configs import settings

NEMOTRON_3_ULTRA = OpenRouterModel(
    model_name="nvidia/nemotron-3-ultra-550b-a55b:free",
    provider=OpenRouterProvider(
        api_key=settings.LLM_API_KEY,
    )
)
