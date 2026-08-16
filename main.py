from highrise import BaseBot, User, Position


class Bot(BaseBot):

    async def on_user_join(self, user: User, position: Position) -> None:
        await self.highrise.chat(
            f"سلام {user.username} 👋 به روم خوش اومدی! ❤️"
        )

    async def on_chat(self, user: User, message: str) -> None:
        msg = message.lower().strip()

        if msg == "!سلام":
            await self.highrise.chat(
                f"سلام {user.username} 😎🤝"
            )

        elif msg == "!help":
            await self.highrise.chat(
                "دستورات بات: !سلام | !help 🤖"
            )
