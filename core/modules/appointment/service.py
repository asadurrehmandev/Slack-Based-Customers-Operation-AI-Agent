from datetime import date, time
from typing import Literal

from sqlalchemy.orm import Session

from core.logger import get_logger
from core.modules.appointment.repository import AppointmentRepository
from core.modules.appointment.validators import AppointmentValidator
from database.models import Appointment

logger = get_logger(__name__)


class AppointmentService:

    @staticmethod
    def get_appointments(
            db: Session,
            start_date: date | None = None,
            end_date: date | None = None,
            start_time: time | None = None,
            end_time: time | None = None,
            status: Literal["all", "confirmed"] = "all"
    ) -> list[Appointment]:
        """
        Get all appointments, Confirmed, Free and Unavailable slots
        """

        if not start_date:
            start_date = date.today()

        logger.debug("GETTING APPOINTMENTS WITH STATUS %s", status)

        return AppointmentRepository.get_appointments(
            db, start_date, end_date, start_time, end_time, status
        )

    @staticmethod
    def get_free_appointments(
            db: Session,
            start_date: date,
            end_date: date | None = None,
            start_time: time | None = None,
            end_time: time | None = None,
    ) -> list[Appointment]:

        effective_date_time_range = AppointmentValidator.get_effective_date_time_range(
            start_date, end_date, start_time, end_time
        )

        if effective_date_time_range is None:
            logger.debug("NO EFFECTIVE TIME RANGE - RETURNING NO APPOINTMENTS")
            return []

        start_date, end_date, start_time, end_time = effective_date_time_range

        logger.debug("GETTING FREE APPOINTMENTS")

        return AppointmentRepository.get_appointments(
            db, start_date, end_date, start_time, end_time, "free"
        )
