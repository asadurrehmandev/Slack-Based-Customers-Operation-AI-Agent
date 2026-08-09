from datetime import date
from typing import Type, List, Dict

from database.models import Appointment


def group_appointments_by_date(
    appointments: list[Appointment],
) -> dict[date, list[Appointment]]:
    """
    Group appointments by appointment date.

    :param appointments:
        List of Appointment model instances.

    :return:
        Dictionary where each date maps to its appointments.
    """

    booked_by_date: dict[date, list[Appointment]] = {}

    for appointment in appointments:
        booked_by_date.setdefault(
            appointment.appointment_date,
            [],
        ).append(appointment)

    return booked_by_date

