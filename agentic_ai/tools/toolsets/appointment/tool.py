from datetime import date, time
from typing import Annotated

from pydantic import Field

from core.logger import get_logger
from . import appointment_toolset
from .schema import AvailableSlots, AvailableSlot

logger = get_logger(__name__)


@appointment_toolset.tool_plain
async def check_available_slots(
        appointment_date: Annotated[
            date,
            Field(description="Date of the appointment")
        ]
) -> AvailableSlots:
    logger.info("Calling check_available_slots tool with date: %s", appointment_date)

    """
    Find available appointment slots on the provided date.

    Args:
        appointment_date: Lookup date of the appointment.

    Returns:
        List of available appointment slots on the provided date.
    """

    mock_slots = {
        date(2026, 8, 10): [
            AvailableSlot(start_time=time(9, 0), end_time=time(9, 30)),
            AvailableSlot(start_time=time(10, 30), end_time=time(11, 0)),
            AvailableSlot(start_time=time(14, 0), end_time=time(14, 30)),
        ],
        date(2026, 8, 8): [
            AvailableSlot(start_time=time(11, 0), end_time=time(11, 30)),
            AvailableSlot(start_time=time(13, 30), end_time=time(14, 0)),
            AvailableSlot(start_time=time(16, 0), end_time=time(16, 30)),
        ],
        date(2026, 8, 12): [
            AvailableSlot(start_time=time(9, 30), end_time=time(10, 0)),
            AvailableSlot(start_time=time(12, 0), end_time=time(12, 30)),
            AvailableSlot(start_time=time(15, 30), end_time=time(16, 0)),
        ],
        date(2026, 8, 13): [
            AvailableSlot(start_time=time(10, 0), end_time=time(10, 30)),
            AvailableSlot(start_time=time(13, 0), end_time=time(13, 30)),
            AvailableSlot(start_time=time(15, 0), end_time=time(15, 30)),
        ],
    }

    return AvailableSlots(
        appointment_date=appointment_date,
        slots=mock_slots.get(appointment_date, []),
    )
