from typing import Annotated, Literal

from pydantic import BaseModel, Field


class SlackAction(BaseModel):
    """
    Interactive action that the user can perform from the Slack notification.
    """

    label: Annotated[
        str,
        Field(
            description="Text displayed on the action button."
        )
    ]

    action_id: Annotated[
        str,
        Field(
            description="Unique identifier used by the backend when this action is clicked."
        )
    ]

    value: Annotated[
        str,
        Field(
            description="Application-specific value associated with the action."
        )
    ]

    style: Annotated[
        Literal["primary", "danger"] | None,
        Field(
            description="Visual style of the button. Use 'primary' for positive actions, 'danger' for destructive actions."
        )
    ] = None


class SlackSection(BaseModel):
    """
    A logical section displayed in the notification.
    """

    title: Annotated[
        str,
        Field(
            description="Short title describing this section."
        )
    ]

    content: Annotated[
        str,
        Field(
            description="Markdown formatted content for this section."
        )
    ]


class SlackNotificationFromTool(BaseModel):
    """
    High-level notification to be rendered as a Slack Block Kit message.
    """

    title: Annotated[
        str,
        Field(
            description="Main heading displayed at the top of the Slack notification."
        )
    ]

    summary: Annotated[
        str,
        Field(
            description="A concise one or two sentence summary of the notification."
        )
    ]

    sections: Annotated[
        list[SlackSection],
        Field(
            description="Additional structured information shown below the summary."
        )
    ] = []

    actions: Annotated[
        list[SlackAction],
        Field(
            description="Interactive actions the user can perform from the notification. Leave empty if no interaction is required."
        )
    ] = []