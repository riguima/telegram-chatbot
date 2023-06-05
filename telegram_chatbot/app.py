import json
import os
import re

from dotenv import load_dotenv
from EdgeGPT import Chatbot, ConversationStyle
from pyrogram.client import Client
from pyrogram.types import Message


load_dotenv()
cookies = json.loads(open('./cookies.json', encoding='utf-8').read())
bots = {}


def create_app() -> Client:
    app = Client(
        os.environ['BOT_NAME'],
        api_id=os.environ['API_ID'],
        api_hash=os.environ['API_HASH'],
    )

    @app.on_message()
    async def chat(client: Client, message: Message):
        username = message.chat.username
        if username not in bots:
            bots[username] = await Chatbot.create(cookies=cookies)
        bot = bots[username]
        response = await bot.ask(
            prompt=message.text,
            conversation_style=ConversationStyle.precise,
        )
        regex = re.compile(r'\[\^\d+\^\]')
        result = regex.sub('', response['item']['result']['message'])
        await message.reply(result)
    return app
