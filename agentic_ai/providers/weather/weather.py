from abc import ABC, abstractmethod

from agentic_ai.providers.weather.schema import WeatherResult


class WeatherProvider(ABC):
    @abstractmethod
    async def get_weather(self, city: str) -> WeatherResult:
        ...


class MockWeatherProvider(WeatherProvider):

    async def get_weather(self, city: str):
        WEATHER_MOCK = {
            "rawalpindi": {
                "temperature": 35,
                "humidity": 90,
                "wind_speed": 2
            },
            "lahore": {
                "temperature": 40,
                "humidity": 80,
                "wind_speed": 0
            },
            "islamabad": {
                "temperature": 30,
                "humidity": 75,
                "wind_speed": 3
            }
        }

        weather = WEATHER_MOCK.get(city.lower())
        if weather is None:
            raise ValueError(f"No weather information found for {city}")

        return WeatherResult(
            temperature=weather["temperature"],
            humidity=weather["humidity"],
            wind_speed=weather["wind_speed"]
        )


class WeatherService:
    def __init__(self, provider: WeatherProvider):
        self.provider = provider

    async def get_weather(self, city: str):
        results = await self.provider.get_weather(city)

        return results
