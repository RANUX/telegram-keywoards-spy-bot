import configparser
import logging

from telethon import TelegramClient, events
from telethon.tl.types import Message
from telethon.tl.functions.channels import JoinChannelRequest

from utils import read_file_lines


class TelegramBot:
    def __init__(self, api_id: int, api_hash: str, phone_number: str, groups_file: str, keywords_file: str, repost_to: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.groups_file = groups_file
        self.keywords_file = keywords_file
        self.groups = read_file_lines(groups_file)
        self.keywords = read_file_lines(keywords_file)
        self.client = TelegramClient(phone_number, api_id, api_hash)
        self.repost_to = repost_to

    def join_groups(self):
        for group in self.groups:
            try:
                self.client(JoinChannelRequest(group))
                logging.info(f"Joined group {group}")
            except Exception as e:
                logging.error(f"Failed to join group {group}: {e}")

    def wait_for_messages(self):
        @self.client.on(events.NewMessage(chats=self.groups))
        async def handler(event):
            message = event.message
            if any(keyword in message.text for keyword in self.keywords):
                await self.repost_message(message)

        self.client.start()
        self.client.run_until_disconnected()

    async def repost_message(self, message: Message):
        entity = await self.client.get_entity(self.repost_to)
        await self.client.send_message(entity, f"Reposting message from {message.chat.title}:\n\n{message.text}")


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    api_id = config.getint("Telegram", "api_id")
    api_hash = config.get("Telegram", "api_hash")
    phone_number = config.get("Telegram", "phone_number")
    groups_file = config.get("Telegram", "groups_file")
    keywords_file = config.get("Telegram", "keywords_file")
    repost_to = config.get("Telegram", "repost_to")

    bot = TelegramBot(api_id, api_hash, phone_number, groups_file, keywords_file, repost_to)
    bot.join_groups()
    bot.wait_for_messages()


if __name__ == "__main__":
    main()
