from dataclasses import dataclass

from core.configs import settings
from integrations.slack.client import OPERATIONS_ASSISTANT
from integrations.slack.services.messenger import SlackMessengerService


@dataclass
class ToolDependencies:
    slack_messenger: SlackMessengerService


deps = ToolDependencies(
    slack_messenger=SlackMessengerService(
        client=OPERATIONS_ASSISTANT,
        default_channel=settings.SLACK_CHANNEL_ID
    )
)
