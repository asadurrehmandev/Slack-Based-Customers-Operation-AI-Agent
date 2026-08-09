from datetime import date, time
from typing import Literal

from sqlalchemy.orm import Session

from core.modules.appointment.validators import AppointmentValidator
from database.models.appointment import AppointmentStatus, Appointment


class AppointmentRepository:

    @staticmethod
    async def get_appointments(
            db: Session,
            start_date: date,
            end_date: date | None = None,
            status: Literal["all", "confirmed", "free"] = "all",
            start_time: time = None,
            end_time: time = None

    ) -> list[Appointment]:

        """
        Get appointments in specified date range.

        :param db: SQLAlchemy session
        :param start_date:
            Start date of appointments
        :param end_date:
            End date of appointments
            Default value is going to be start_date
        :param status:
            Appointments status to filter
            all, confirmed, free

        :return:
            List of appointments

        :raises ValueError:
            If the start_date and end_date are in past or not correct.
        """

        if not end_date:
            end_date = start_date

        AppointmentValidator.validate_dates(
            start_date=start_date,
            end_date=end_date,
        )

        query = db.query(Appointment).filter(
            Appointment.appointment_date >= start_date,
            Appointment.appointment_date <= end_date,
        )

        if status == "free":
            ...

        if status == "confirmed":
            query = query.filter(
                Appointment.appointment_status
                == AppointmentStatus(status)
            )

        return query.all()


if __name__ == "__main__":
    import asyncio


    async def main():
        from database import get_db

        db = get_db()
        appointments = await AppointmentRepository.get_appointments(
            db=next(db),
            start_date=date(2026, 8, 8)
        )

        print(appointments)


    asyncio.run(main())
