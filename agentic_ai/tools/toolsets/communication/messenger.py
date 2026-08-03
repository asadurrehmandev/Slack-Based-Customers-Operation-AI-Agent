from typing import Annotated, Literal

from pydantic import Field
from pydantic_ai import RunContext

from agentic_ai.providers.messenger.schema import MessengerResult
from agentic_ai.tools.toolsets.dependencies import ToolDependencies
from . import communication_toolset


@communication_toolset.tool
async def send_message(
        ctx: RunContext[ToolDependencies],
        platform: Annotated[
            Literal["whatsapp", "telegram"],
            Field(description="Messaging platform to use.")
        ],
        recipient: Annotated[
            str,
            Field(description="Recipient name, phone number, username, or channel.")
        ],
        message: Annotated[
            str,
            Field(description="The message content to send.")
        ]
) -> MessengerResult:
    """
        Send a message to a recipient using a supported messaging platform.

        Use this tool whenever the user asks to:

        - Send a WhatsApp message
        - Send a Telegram message
        - Deliver a text message
        - Notify someone through a supported messaging platform

        Args:
            platform:
                Messaging platform to use.

            recipient:
                Recipient identifier. Depending on the provider this may be
                a phone number, username, channel or contact name.

            message:
                The message content to send.

        Returns:
            MessengerResult containing:

            - delivery status
            - messaging platform used
            - execution description

        Raises:
            ValueError:
                If the requested messaging platform is not supported.
        """

    return await ctx.deps.messenger_service.send(
        platform=platform,
        recipient=recipient,
        message=message
    )
