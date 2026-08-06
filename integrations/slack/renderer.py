from typing import List

from agentic_ai.tools.toolsets.slack.schema import SlackNotificationFromTool
from integrations.slack.schema import (
    SlackMessage,
    HeaderBlock,
    PlainText,
    DividerBlock,
    SectionBlock,
    MarkdownText,
    ActionsBlock,
    ButtonElement, SlackBlock,
)

from core.logger import get_logger

logger = get_logger(__name__)

class SlackRenderer:

    @staticmethod
    def render_header(content: str) -> HeaderBlock:
        return HeaderBlock(
            text=PlainText(
                text=content
            )
        )

    @staticmethod
    def render_section(content: str) -> SectionBlock:
        return SectionBlock(
            text=MarkdownText(
                text=content
            )
        )

    @staticmethod
    def render_button(action) -> ButtonElement:
        return ButtonElement(
            type="button",
            text=PlainText(
                text=action.label
            ),
            action_id=action.action_id,
            value=action.value,
            style=action.style
        )

    @staticmethod
    def render(notification: SlackNotificationFromTool) -> SlackMessage:

        logger.info("Rendering Slack notification provided by AI.")

        blocks: List[SlackBlock] = [
            SlackRenderer.render_header(notification.title)
            ,
            DividerBlock(),
            SlackRenderer.render_section(notification.summary),
        ]

        for section in notification.sections:
            blocks.extend([
                DividerBlock(),
                SlackRenderer.render_section(f"*{section.title}*\n{section.content}"),
            ])

        if notification.actions:
            blocks.append(
                DividerBlock()
            )

            blocks.append(
                ActionsBlock(
                    elements=[
                        SlackRenderer.render_button(action)
                        for action in notification.actions
                    ]
                )
            )

        return SlackMessage(
            text=notification.title,
            blocks=blocks,
        )
