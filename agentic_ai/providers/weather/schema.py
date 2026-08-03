from typing import Annotated

from pydantic import BaseModel, Field


class WeatherResult(BaseModel):
    temperature: Annotated[
        float,
        Field(gt=0, description="Climate Temperature of the City in Celsius")
    ]
    humidity: Annotated[
        float,
        Field(gt=0, description="Humidity of the City in %")
    ]
    wind_speed: Annotated[
        float,
        Field(gt=-1, description="Wind speed of the City in m/s")
    ]

    def __str__(self):
        return (
            f"""
-----------------------------
     WEATHER BREAKDOWN
-----------------------------
TEMPERATURE: {self.temperature} C
HUMIDITY: {self.humidity} %
WIND SPEED: {self.wind_speed} m/s
            """
        )
