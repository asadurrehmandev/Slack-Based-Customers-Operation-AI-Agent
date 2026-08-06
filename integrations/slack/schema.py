from typing import Annotated, Literal

from pydantic import BaseModel, Field


class PlainText(BaseModel):
    type: Literal["plain_text"] = "plain_text"

    text: Annotated[
        str,
        Field(description="Plain text displayed in Slack.")
    ]

    emoji: bool = True


class MarkdownText(BaseModel):
    type: Literal["mrkdwn"] = "mrkdwn"

    text: Annotated[
        str,
        Field(description="Markdown formatted text displayed in Slack.")
    ]


class HeaderBlock(BaseModel):
    type: Literal["header"] = "header"

    text: PlainText


class SectionBlock(BaseModel):
    type: Literal["section"] = "section"

    text: PlainText | MarkdownText


class DividerBlock(BaseModel):
    type: Literal["divider"] = "divider"


class ButtonElement(BaseModel):
    type: Literal["button"] = "button"

    text: PlainText

    action_id: str

    value: str

    style: Literal["primary", "danger"] | None = None


class ActionsBlock(BaseModel):
    type: Literal["actions"] = "actions"

    elements: list[ButtonElement]


SlackBlock = (
        HeaderBlock
        | SectionBlock
        | DividerBlock
        | ActionsBlock
)


class SlackMessage(BaseModel):
    text: Annotated[
        str,
        Field(description="Message text displayed in Slack, i.e New Customer Email or New Office Policy")
    ]

    blocks: list[SlackBlock]


SLACK_TEMPLATE_MESSAGE = SlackMessage(
    text="📧 New Email Received",
    blocks=[
        HeaderBlock(
            text=PlainText(
                text="📧 New Customer Email"
            )
        ),

        DividerBlock(),

        SectionBlock(
            text=MarkdownText(
                text=(
                    "*From:* John Doe\n"
                    "*Email:* john.doe@example.com\n"
                    "*Subject:* Refund Request\n\n"
                    "Hello,\n"
                    "I purchased your product yesterday and would like to request "
                    "a refund because I accidentally bought the wrong plan."
                )
            )
        ),

        DividerBlock(),

        SectionBlock(
            text=MarkdownText(
                text=(
                    "*AI Summary*\n"
                    "• Intent: Refund Request\n"
                    "• Priority: Medium\n"
                    "• Confidence: 97%\n"
                    "• Suggested Department: Billing"
                )
            )
        ),

        DividerBlock(),

        ActionsBlock(
            elements=[
                ButtonElement(
                    text=PlainText(
                        text="Approve Reply"
                    ),
                    action_id="approve_reply",
                    value="email_12345",
                    style="primary",
                ),
                ButtonElement(
                    text=PlainText(
                        text="Reject"
                    ),
                    action_id="reject_reply",
                    value="email_12345",
                    style="danger",
                ),
                ButtonElement(
                    text=PlainText(
                        text="Assign Agent"
                    ),
                    action_id="assign_agent",
                    value="email_12345",
                ),
            ]
        ),
    ],
)
