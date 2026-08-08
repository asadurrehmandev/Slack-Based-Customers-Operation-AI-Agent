from slack_sdk.web.async_client import AsyncWebClient

from core.configs import settings

# FOR NAME EASE, WE CAN'T DEFINE AsyncWebClient AS A TYPE EVERYWHERE DUE TO NAME CONFUSION
SlackBot = AsyncWebClient

OPERATIONS_ASSISTANT = AsyncWebClient(
    token=settings.SLACK_BOT_OPERATIONS_ASSISTANT_TOKEN,
)
