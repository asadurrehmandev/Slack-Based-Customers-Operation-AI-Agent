from dataclasses import dataclass

from agentic_ai.providers.messenger.messenger import MessengerService, MessengerProviderFactory
from agentic_ai.providers.weather.weather import WeatherService, MockWeatherProvider


@dataclass
class ToolDependencies:
    weather_service: WeatherService
    messenger_service: MessengerService


deps = ToolDependencies(
    # Weather Service
    weather_service=WeatherService(
        provider=MockWeatherProvider()
    ),

    # Whatsapp/Telegram and Other Messaging Service
    messenger_service=MessengerService(
        factory=MessengerProviderFactory()
    )
)
