from agentic_ai.agents.base import create_agent
from agentic_ai.agents.prompt_builder import build_prompt
from agentic_ai.model.openrouter_free import OPENROUTER_FREE
from agentic_ai.tools.toolsets.appointment import appointment_toolset
from agentic_ai.tools.toolsets.dependencies import ReceptionistDependencies
from agentic_ai.tools.toolsets.utils import utils_toolset

SYSTEM_PROMPT = build_prompt(
    "receptionist/receptionist.md",
    "business.md",
    "receptionist/example.md",
    "personality.md",
    "safety.md",
)

receptionist_agent = create_agent(
    model=OPENROUTER_FREE,
    prompt=SYSTEM_PROMPT,
    toolsets=[
        appointment_toolset,
        utils_toolset,
    ],
    deps_type=ReceptionistDependencies,
)

if __name__ == "__main__":
    import asyncio


    async def main():
        message_history = []

        from database import get_db

        print("Receptionist Agent")
        print("Type 'exit' to quit.\n")

        db = next(get_db())

        deps = ReceptionistDependencies(db=db)

        try:
            while True:
                prompt = input("You: ").strip()

                if prompt.lower() in {"exit", "quit"}:
                    break

                result = await receptionist_agent.run(
                    prompt,
                    deps=deps,
                    message_history=message_history,
                )

                print(f"\nAssistant: {result.output}\n")

                # Keep the conversation for the next turn
                message_history = result.all_messages()
        finally:
            db.close()


    asyncio.run(main())
