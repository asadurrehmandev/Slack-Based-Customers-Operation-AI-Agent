from datetime import date, time
from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class AvailableSlot(BaseModel):
    slot_id: UUID = Field(
        description="Unique identifier of the available appointment slot. "
                    "Use this ID when booking the selected slot."
    )
    start_time: time = Field(
        description="Start time of the available appointment slot."
    )
    end_time: time = Field(
        description="End time of the available appointment slot."
    )


class AvailableDate(BaseModel):
    appointment_date: date = Field(
        description="Date on which the appointment slots are available."
    )
    slots: list[AvailableSlot] = Field(
        description="Available appointment time slots for this date."
    )


class AvailableAppointments(BaseModel):
    appointments: list[AvailableDate] = Field(
        description="Available appointment dates and their available time slots."
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
