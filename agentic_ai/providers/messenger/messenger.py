from abc import ABC
from typing import Type

from agentic_ai.providers.messenger.schema import MessengerResult


class Messenger(ABC):
    def send(self, recipient: str, message: str) -> MessengerResult:
        ...


class WhatsAppMessenger(Messenger):
    async def send(self, recipient: str, message: str):
        return MessengerResult(
            status=True,
            messenger_platform="whatsapp",
            description="Message sent successfully"
        )


class TelegramMessenger(Messenger):
    async def send(self, recipient: str, message: str):
        return MessengerResult(
            status=True,
            messenger_platform="telegram",
            description="Message sent successfully"
        )


class MessengerProviderFactory:
    def __init__(self):
        self.providers = {
            "whatsapp": WhatsAppMessenger(),
            "telegram": TelegramMessenger(),
        }

    def get(self, platform: str) -> Messenger:
        return self.providers[platform]


class MessengerService:

    def __init__(self, factory: MessengerProviderFactory):
        self.factory = factory

    async def send(self, recipient: str, message: str, platform: str):
        messenger = self.factory.get(platform)

        print(
            "SENDING MESSAGE TO: {}".format(recipient),
        )
        print(
            "MESSAGE CONTENT: {}".format(message),
        )
        print(
            "MESSAGE PLATFORM: {}".format(platform),
        )

        return await messenger.send(recipient=recipient, message=message)


if __name__ == "__main__":

    import asyncio

    async def main():
        messenger = MessengerService(
            factory=MessengerProviderFactory()
        )

        whatsapp_response = await messenger.send(
            recipient="Asad Ur Rehman",
            message="Hello World!",
            platform="whatsapp",
        )

        telegram_response = await messenger.send(
            recipient="Asad Ur Rehman",
            message="Hello World!",
            platform="telegram",
        )

        print(whatsapp_response)
        print(telegram_response)

    asyncio.run(main())