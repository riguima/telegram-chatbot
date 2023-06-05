import json
import os
import re

from dotenv import load_dotenv
from EdgeGPT import Chatbot, ConversationStyle
from pyrogram.client import Client
from pyrogram.types import Message


load_dotenv()
cookies = json.loads(open('./cookies.json', encoding='utf-8').read())
bots = []
usernames = []


def create_app() -> Client:
    app = Client(
        os.environ['BOT_NAME'],
        api_id=os.environ['API_ID'],
        api_hash=os.environ['API_HASH'],
    )

    @app.on_message()
    async def chat(client: Client, message: Message):
        if message.chat.username not in usernames:
            bots.append(await Chatbot.create(cookies=cookies))
            usernames.append(message.chat.username)
        bot = bots[usernames.index(message.chat.username)]
        response = await bot.ask(
            prompt=message.text,
            conversation_style=ConversationStyle.precise,
        )
        regex = re.compile(r'\[\^\d+\^\]')
        result = regex.sub('', response['item']['result']['message'])
        await message.reply(result)
    return app
