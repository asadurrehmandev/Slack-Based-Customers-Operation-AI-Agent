from pydantic_ai import FunctionToolset

slack_toolset = FunctionToolset(id="slack")

from . import messenger
