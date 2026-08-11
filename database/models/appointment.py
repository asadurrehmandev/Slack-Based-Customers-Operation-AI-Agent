from datetime import date, datetime, time
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum as PGEnum, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.connection import DatabaseBase


class AppointmentStatus(str, Enum):
    CONFIRMED = "confirmed"
    FREE = "free"


class Appointment(DatabaseBase):
    __tablename__ = "appointments"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    # CUSTOMER INFO
    customer_name: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    customer_email: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    # APPOINTMENT INFO
    appointment_date: Mapped[date] = mapped_column(
        nullable=False,
    )

    start_time: Mapped[time] = mapped_column(
        nullable=False,
    )

    end_time: Mapped[time] = mapped_column(
        nullable=False,
    )

    appointment_status: Mapped[AppointmentStatus] = mapped_column(
        PGEnum(AppointmentStatus),
        default=AppointmentStatus.FREE,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    calendar_sync_job: Mapped["CalendarSyncJob | None"] = relationship(
        back_populates="appointment",
        uselist=False,
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"<Appointment("
            f"id={self.id}, "
            f"date={self.appointment_date}, "
            f"start={self.start_time}, "
            f"end={self.end_time}, "
            f"status={self.appointment_status}"
            f")>"
        )
