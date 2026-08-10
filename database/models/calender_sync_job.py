from datetime import datetime
from enum import Enum
from uuid import uuid4, UUID

from sqlalchemy import ForeignKey, String, Enum as PGEnum, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import DatabaseBase


class CalendarSyncStatus(str, Enum):
    PENDING = "pending"
    SYNCED = "synced"
    FAILED = "failed"


class CalenderSyncJob(DatabaseBase):
    __tablename__ = "calender_sync_job"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    appointment_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("appointments.id"),
        nullable=False,
    )

    calender_event_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    status: Mapped[CalendarSyncStatus] = mapped_column(
        PGEnum(CalendarSyncStatus),
        default=CalendarSyncStatus.PENDING,
        nullable=False,
    )

    attempts: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    appointment: Mapped["Appointment"] = relationship(
        back_populates="calendar_sync_job",
    )
