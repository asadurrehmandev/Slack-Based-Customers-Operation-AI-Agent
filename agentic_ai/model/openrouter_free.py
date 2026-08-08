from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

from core.configs import settings

OPENROUTER_FREE = OpenRouterModel(
    model_name="openrouter/free",
    provider=OpenRouterProvider(
        api_key=settings.LLM_API_KEY,
        app_url="http://localhost:8000",
        app_title="AI Receptionist Dev"
    )
)
