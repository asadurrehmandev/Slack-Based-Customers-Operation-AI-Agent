from typing import Sequence

from pydantic_ai import Agent, FunctionToolset
from pydantic_ai.models.openrouter import OpenRouterModel

from core.logger import get_logger

logger = get_logger(__name__)


def create_agent(
        *,
        model: OpenRouterModel,
        prompt: str,
        toolsets: Sequence[FunctionToolset] | None = None,
        deps_type: type | None = None,
) -> Agent:

    logger.info(f"Creating agent with Model: {model}")

    kwargs = {
        "model": model,
        "system_prompt": prompt,
    }

    if toolsets:
        kwargs["toolsets"] = list(toolsets)

    if deps_type is not None:
        kwargs["deps_type"] = deps_type

    return Agent(**kwargs)
