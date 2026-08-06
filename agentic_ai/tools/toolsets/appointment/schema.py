from datetime import date, time
from typing import Annotated, Optional

from pydantic import BaseModel, Field


class AvailableSlot(BaseModel):
    start_time: time = Field(
        description="Start time of the available appointment slot."
    )

    end_time: time = Field(
        description="End time of the available appointment slot."
    )


class AvailableSlots(BaseModel):
    appointment_date: date = Field(
        description="The date these appointment slots are available."
    )

    slots: list[AvailableSlot] = Field(
        description="List of all available appointment slots for the specified date."
    )


# THIS IS WHAT AI WILL ASK FROM THE USER
class AppointmentRequest(BaseModel):
    customer_name: Annotated[
        str,
        Field(description="Name of the client who want to book the appointment")
    ]
    email: Annotated[
        str,
        Field(description="Email of the client who want to book the appointment")
    ]
    phone: Annotated[
        str,
        Field(description="Phone of the client who want to book the appointment")
    ]

    service: Annotated[
        str,
        Field(description="Why the client want to book the appointment")
    ]

    appointment_date: Annotated[
        date,
        Field(description="Date of the appointment")
    ]

    start_time: Annotated[
        time,
        Field(description="Start time of the appointment")
    ]

    notes: Annotated[
        Optional[str],
        Field(description="Additional information about the appointment")
    ]
