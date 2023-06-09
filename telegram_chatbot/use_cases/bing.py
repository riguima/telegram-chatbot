import re
import asyncio

from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle


class BingChatbot:
    def __init__(self, chatbot: Chatbot) -> None:
        self.chatbot = chatbot

    async def ask(self, message: str) -> str:
        response = await self.chatbot.ask(
            prompt=message,
            conversation_style=ConversationStyle.creative,
            simplify_response=True,
        )
        formatted_response = self.format_message(response['text'])
        return formatted_response

    def format_message(self, message: str) -> str:
        regex = re.compile(r'\[\^\d+\^\]')
        return regex.sub('', message)
