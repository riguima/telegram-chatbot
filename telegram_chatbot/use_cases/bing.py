import os
import re
import asyncio

from dotenv import load_dotenv
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from EdgeGPT.ImageGen import ImageGenAsync


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

    async def generate_images(self, message: str) -> str:
        load_dotenv()
        async with ImageGenAsync(os.environ['AUTH_COOKIE'], True) as image_generator:
            images = await image_generator.get_images(message)
            await image_generator.save_images(images, output_dir='images')
