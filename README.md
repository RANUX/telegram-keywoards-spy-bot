# Telegram keywords spy bot

A Telegram bot that can join groups, wait for messages in those groups, and repost messages containing specific keywords to the bot owner.

### Core classes, functions, and methods
- `TelegramBot`: A class representing the Telegram bot, responsible for joining groups, waiting for messages, and reposting messages.
  - `__init__(self, api_id: int, api_hash: str, phone_number: str, groups_file: str, keywords_file: str, repost_to: str)`: Constructor that initializes the bot with the given API credentials, phone number, and file paths for the groups and keywords.
  - `join_groups(self)`: Method that joins the groups listed in the groups file.
  - `wait_for_messages(self)`: Method that waits for messages in the joined groups and reposts messages containing keywords to the bot owner.
  - `repost_message(self, message: Message)`: Method that reposts the given message to the bot owner.
- `main()`: The entry point of the program, responsible for creating and running the Telegram bot.

The project will have the following files:
- `requirements.txt`: A file containing the required Python packages for the project.
- `config.ini`: A configuration file containing the API credentials and phone number for the Telegram bot.
- `telegram_bot.py`: The main module containing the `TelegramBot` class and the `main()` function.
- `utils.py`: A module containing utility functions for reading the groups and keywords files.

### How to install
```
make install
```

### Signing In
Before working with Telegram’s API, you need to get your own API ID and hash:

Login to [your Telegram account](https://my.telegram.org) with the phone number of the developer account to use.
Click under API Development tools.
A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!
Note

> This API ID and hash is the one used by your application, not your phone number. You can use this API ID and hash with any phone number or even for bot accounts.

### How to run
Change config.ini, groups.txt and keywords.txt
```
make run
```

### Build docker image
```
docker build -t spybot .
```

## Run docker image
```
docker run -d spybot
```