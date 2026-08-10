from datetime import date, time
from typing import Literal

from sqlalchemy.orm import Session

from database.models.appointment import AppointmentStatus, Appointment

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