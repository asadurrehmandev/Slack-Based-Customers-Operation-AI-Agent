from uuid import UUID

from sqlalchemy.orm import Session

from core.logger import get_logger
from database.models import CalendarSyncJob

logger = get_logger(__name__)


class CalendarSyncRepository:

    @staticmethod
    def add_sync(
            db: Session,
            appointment_id: UUID
    ) -> CalendarSyncJob:
        """
        Add a calendar sync job record to database
        :param db: SqlAlchemy session
        :param appointment_id: Verified appointment id
        :return: Calendar Sync Object
        """

        sync_job = CalendarSyncJob(
            appointment_id=appointment_id,
        )

        db.add(sync_job)

        logger.debug("Adding calendar sync job for appointment: %s", appointment_id)

        return sync_job
