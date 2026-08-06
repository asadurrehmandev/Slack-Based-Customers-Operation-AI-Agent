from pathlib import Path

from core.logger import get_logger

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

logger = get_logger(__name__)


def load_prompt(
        prompt_filename: str
) -> str:
    return (
            PROMPTS_DIR / prompt_filename
    ).read_text(encoding="utf-8")


def build_prompt(*files: str) -> str:
    logger.info("Building prompt for the agent")
    return "\n\n".join(load_prompt(f) for f in files)
