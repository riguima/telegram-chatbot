import re

from httpx import Client


class BingChatbot:
    def ask(self, message: str) -> str:
        with Client() as client:
            response = client.post(
                'http://89.116.225.24:8005/send-message',
                headers={'Content-type': 'application/x-www-form-urlencoded'},
                data={'message': message},
                timeout=None,
            )
            formatted_response = self.format_message(response.json()['data'])
            return formatted_response

    def format_message(self, message: str) -> str:
        regex = re.compile(r'\[\^\d+\^\]')
        return regex.sub('', message)
