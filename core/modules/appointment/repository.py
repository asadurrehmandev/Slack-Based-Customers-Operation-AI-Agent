from datetime import date, time
from typing import Literal
from uuid import UUID

from sqlalchemy.orm import Session

from core.logger import get_logger
from core.modules.calender_sync.repository import CalendarSyncRepository
from core.modules.exceptions import AppointmentException
from database.models.appointment import AppointmentStatus, Appointment

logger = get_logger(__name__)

AppointmentStatusFilter = Literal[
    "all",
    "confirmed",
    "free"
]


class AppointmentRepository:

    @staticmethod
    def get_appointments(
            db: Session,
            start_date: date,
            end_date: date | None = None,
            start_time: time | None = None,
            end_time: time | None = None,
            status: AppointmentStatusFilter = "all",
    ) -> list[Appointment]:
        """
        Get appointments from the database within the specified
        date and optional time range.

        ``end_date`` is inclusive.

        ``status="all"`` returns appointments regardless of status.

        ``status="confirmed"`` returns only confirmed appointments.
        """

        # If no end date is provided, search only start_date.
        end_date = end_date or start_date

        query = db.query(Appointment).filter(
            Appointment.appointment_date >= start_date,
            Appointment.appointment_date <= end_date,
        )

        if start_time is not None:
            query = query.filter(
                Appointment.start_time >= start_time,
            )

        if end_time is not None:
            query = query.filter(
                Appointment.end_time <= end_time,
            )

        if status != "all":
            query = query.filter(
                Appointment.appointment_status
                == AppointmentStatus(status),
            )

        return query.all()

    @staticmethod
    def get_appointment(
            db: Session,
            appointment_id: UUID
    ):
        query = db.get(Appointment, appointment_id)
        if not query:
            logger.warning(f"No appointment with id {appointment_id}")
            raise AppointmentException(f"No appointment with id {appointment_id}", error_code=404)

        return query

    @staticmethod
    def book_appointment(
            db: Session,
            appointment_id: UUID,
            customer: dict
    ):

        appointment = AppointmentRepository.get_appointment(db, appointment_id)

        try:
            appointment.status = AppointmentStatus.CONFIRMED
            appointment.customer_name = customer.get("customer_name")
            appointment.customer_id = customer.get("customer_id")

            db.flush()

            sync_job = CalendarSyncRepository.add_sync(db, appointment_id)
            db.commit()

        except Exception as e:
            logger.error(e)
            db.rollback()

if __name__ == "__main__":

    from database import get_db

    appointment_id = "cb780436-662a-4e57-83a8-cfc0e8225926"
    appointment = AppointmentRepository.get_appointment(
        db = next(get_db()),
        appointment_id = appointment_id,
    )

    print(appointment)