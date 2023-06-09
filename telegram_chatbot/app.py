import json
import os

from dotenv import load_dotenv
from EdgeGPT.EdgeGPT import Chatbot
from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram import filters

from telegram_chatbot.use_cases.bing import BingChatbot


def create_app() -> Client:
    load_dotenv()
    app = Client(
        os.environ['BOT_NAME'],
        api_id=os.environ['API_ID'],
        api_hash=os.environ['API_HASH'],
    )
    users_data = {}

    @app.on_message()
    async def ask(client: Client, message: Message) -> None:
        searching = await message.reply('Pesquisando...')
        username = message.chat.username
        if username not in users_data:
            cookies = json.load(open('cookies.json', encoding='utf-8'))
            bot = await Chatbot.create(cookies=cookies)
            chatbot = BingChatbot(bot)
            users_data[username] = {
                'chatbot': chatbot
            }
        else:
            chatbot = users_data[username]['chatbot']
        response = await chatbot.ask(message.text)
        await message.reply(response)
        await searching.delete()
    return app
