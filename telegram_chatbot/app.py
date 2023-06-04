import asyncio
import json
import os
import re

from dotenv import load_dotenv
from EdgeGPT import Chatbot, ConversationStyle
from pyrogram.client import Client
from pyrogram.types import Message


load_dotenv()
cookies = json.loads(open('./cookies.json', encoding='utf-8').read())


def create_app() -> Client:
    app = Client(
        os.getenv('BOT_NAME'),
        api_id=os.getenv('API_ID'),
        api_hash=os.getenv('API_HASH'),
    )
    @app.on_message()
    async def chat(client: Client, message: Message):
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt=message.text,
            conversation_style=ConversationStyle.precise,
        )
        regex = re.compile(r'\[\^\d+\^\]')
        result = regex.sub('', response['item']['result']['message'])
        await message.reply(result)
        await bot.close()
    return app
