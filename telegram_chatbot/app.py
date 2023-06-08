import os

from dotenv import load_dotenv
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

    chatbot = BingChatbot()

    @app.on_message()
    async def ask(client: Client, message: Message) -> None:
        searching = await message.reply('Pesquisando...')
        await message.reply(chatbot.ask(message.text))
        await searching.delete()
    return app
