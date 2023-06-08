import pytest

from telegram_chatbot.use_cases.bing import BingChatbot


@pytest.fixture(scope='module')
def chatbot() -> BingChatbot:
    return BingChatbot()


def test_ask(chatbot: BingChatbot) -> None:
    response = chatbot.ask('Quantas Champions o messi já conquistou?')
    assert (
        'Lionel Messi conquistou quatro títulos da Liga dos Campeões da UEFA'
    ) in response
