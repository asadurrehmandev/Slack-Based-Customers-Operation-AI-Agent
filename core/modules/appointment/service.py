from datetime import date, time
from typing import Literal

from sqlalchemy.orm import Session

from core.logger import get_logger
from core.modules.appointment.repository import AppointmentRepository
from database.models import Appointment

logger = get_logger(__name__)


class AppointmentService:

    @staticmethod
    def get_appointments(
            db: Session,
            start_date: date,
            end_date: date | None = None,
            start_time: time | None = None,
            end_time: time | None = None,
            status: Literal["all", "confirmed"] = "all"
    ) -> list[Appointment]:
        """
        Get all appointments, Confirmed, Free and Unavailable slots
        """

        logger.debug("GETTING APPOINTMENTS WITH STATUS %s", status)

        return AppointmentRepository.get_appointments(
            db, start_date, end_date, status, start_time, end_time
        )
