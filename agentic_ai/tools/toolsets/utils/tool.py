from datetime import date

from core.logger import get_logger
from . import utils_toolset

logger = get_logger(__name__)


@utils_toolset.tool_plain
async def get_current_date() -> date:
    logger.info("Calling get_current_date Tool")
    return date.today()
