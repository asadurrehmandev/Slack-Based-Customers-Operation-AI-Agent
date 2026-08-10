from datetime import date
from typing import Annotated, Optional

from pydantic import Field
from pydantic_ai import RunContext

from core.logger import get_logger
from core.modules.appointment.service import AppointmentService
from . import appointment_toolset
from .schema import AvailableAppointments, AvailableSlot, AvailableDate
from ..dependencies import ReceptionistDependencies

logger = get_logger(__name__)


@appointment_toolset.tool
async def check_available_slots(
        ctx: RunContext[ReceptionistDependencies],
        start_date: Annotated[
            date,
            Field(
                description=(
                        "The date from which to search for available appointments. "
                        "This date is included in the search."
                )
            ),
        ],
        end_date: Annotated[
            Optional[date],
            Field(
                description=(
                        "Optional final date for the availability search. "
                        "This date is included. If omitted, only start_date is searched."
                )
            ),
        ] = None,
) -> AvailableAppointments:
    """
        Find available appointment slots within the requested date range.

        The search includes start_date and, when provided, end_date.
        Past dates and past times are automatically excluded.

        Args:
            ctx:
                Pydantic AI run context containing the AppointmentService.

            start_date:
                First date to check for available appointment slots.

            end_date:
                Optional final date to check. If omitted, only start_date
                is searched.

        Returns:
            AvailableAppointments:
                A list of dates containing their available appointment slots.
                Returns an empty appointments list when no slots are available.
        """

    logger.debug(
        "CHECKING AVAILABLE SLOTS | start_date=%s, end_date=%s",
        start_date,
        end_date,
    )

    appointments = AppointmentService.get_free_appointments(
        db=ctx.deps.db,
        start_date=start_date,
        end_date=end_date,
    )

    available_dates: dict[date, list[AvailableSlot]] = {}

    for appointment in appointments:
        available_dates.setdefault(
            appointment.appointment_date,
            [],
        ).append(
            AvailableSlot(
                slot_id=appointment.id,
                start_time=appointment.start_time,
                end_time=appointment.end_time,
            )
        )

    return AvailableAppointments(
        appointments=[
            AvailableDate(
                appointment_date=appointment_date,
                slots=slots,
            )
            for appointment_date, slots in available_dates.items()
        ]
    )
