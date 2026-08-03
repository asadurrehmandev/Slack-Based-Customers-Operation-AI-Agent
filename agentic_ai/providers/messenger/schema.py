from typing import Annotated

from pydantic import BaseModel, Field


class MessengerResult(BaseModel):
    status: Annotated[
        bool,
        Field(description="Tells if the message was sent successfully"),
    ]

    messenger_platform: Annotated[
        str,
        Field(description="The platform that the message was sent to"),
    ]

    description: Annotated[
        str,
        Field(description="Details about the message status")
    ]