from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from configs import settings

OPENROUTER_FREE = OpenRouterModel(
    model_name="openrouter/free",
    provider=OpenRouterProvider(
        api_key=settings.LLM_API_KEY
    )
)
