from pydantic_ai import RunContext

from . import slack_toolset
from .schema import SlackNotificationFromTool
from ..dependencies import ToolDependencies
from core.logger import get_logger

logger = get_logger(__name__)


@slack_toolset.tool
async def post_slack_message(
        ctx: RunContext[ToolDependencies],
        message: SlackNotificationFromTool,
):

    logger.info(f"Calling the tool: post_slack_message")

    """
    Send a message to a Slack channel.

    Use this tool whenever information should be shared with users in Slack.

    Examples:
    - Notify the team about a newly received customer email.
    - Send an AI-generated summary.
    - Post task assignments.
    - Request human approval using interactive buttons.
    - Announce system alerts or deployment status.
    - Share reports, reminders, or workflow updates.

    Do not use this tool to answer the user directly. Use it only when the
    information should be delivered to Slack.

    Args:
        message:
            A complete Slack message.

            The message should contain:
            - text: A plain-text fallback used by Slack notifications.
            - blocks: The Slack Block Kit layout that users will see.

            Include interactive buttons when users need to perform an action,
            such as Approve, Reject, Assign, or Reply.

    Returns:
        Information about the Slack API response after the message is sent.
    """

    return await ctx.deps.slack_messenger.send_message(
        message=message
    )
