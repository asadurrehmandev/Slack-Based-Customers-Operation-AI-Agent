from pydantic_ai import FunctionToolset

utils_toolset = FunctionToolset(id="utils")

from .tool import *