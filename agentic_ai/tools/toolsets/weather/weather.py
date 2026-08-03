from typing import Annotated

from pydantic import Field
from pydantic_ai import RunContext

from agentic_ai.providers.weather.schema import WeatherResult
from . import weather_toolset
from ..dependencies import ToolDependencies


@weather_toolset.tool
async def get_current_weather(
        ctx: RunContext[ToolDependencies],
        city: Annotated[
            str,
            Field(description="Name of the city to fetch weather for")
        ]
) -> WeatherResult:
    """
    Get the current weather for a city.

    Use this tool whenever a user asks:

    - What is the weather?
    - Weather forecast
    - Temperature
    - Humidity
    - Wind speed

    Args:
        city:
            Name of the city.

    Returns:
        Current weather information.
    """

    return await ctx.deps.weather_service.get_weather(city)
