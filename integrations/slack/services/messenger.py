from agentic_ai.tools.toolsets.slack.schema import SlackNotificationFromTool
from core.logger import get_logger
from integrations.slack.client import OPERATIONS_ASSISTANT, SlackBot
from integrations.slack.renderer import SlackRenderer
from integrations.slack.schema import SLACK_TEMPLATE_MESSAGE

logger = get_logger(__name__)

class SlackMessengerService:

    def __init__(self
                 , client: SlackBot
                 , default_channel: str):
        self.client = client
        self.default_channel = default_channel

    async def send_message(self,
                           *,
                           channel: str = None,
                           message: SlackNotificationFromTool):
        """
        Send a Slack message.

        Args:
            channel:
                Slack channel ID.

            message:
                Slack message payload.
        """

        rendered_message = SlackRenderer.render(message)

        logger.info(f"Sending Slack message")

        return await self.client.chat_postMessage(
            channel=channel or self.default_channel,
            **rendered_message.model_dump(exclude_none=True)
        )


if __name__ == "__main__":
    import asyncio


    async def main():
        from core.configs import settings

        slack_messenger = SlackMessengerService(
            client=OPERATIONS_ASSISTANT,
            default_channel=settings.SLACK_CHANNEL_ID
        )

        results = await slack_messenger.send_message(
            message=SLACK_TEMPLATE_MESSAGE
        )

        print(results)


    asyncio.run(main())
