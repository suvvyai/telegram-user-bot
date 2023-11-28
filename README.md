# Telegram User Bot for Suvvy AI

## About
The `telegram-user-bot` is an integration tool designed for Suvvy AI. This project allows seamless interaction between Telegram and Suvvy AI via user bot, providing an efficient and user-friendly platform for communication.

## Installation
Clone the repository and install the dependencies:
```shell
pipx install git+https://github.com/suvvyai/telegram-user-bot
suvvyuser --help
```

## Usage
```shell
suvvyuser  # using ./config.json
# or
suvvyuser --config CONFIG_PATH
```

## Configuration
```shell
wget https://github.com/suvvyai/telegram-user-bot/blob/main/config.example.json -O config.json
nano config.json
```
```json
{
  "api_id": 0,
  "api_hash": "",
  "phone_number": "",
  "suvvy_api_key": "",
  "timeouts": {
    "before_read_seconds": 0,
    "before_answer_seconds": 0
  }
}
```
- **api_id** and **api_hash** can be obtained from https://my.telegram.org/apps
- **suvvy_api_key** can be obtained from https://home.suvvy.ai

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any queries or suggestions, please open an issue in the GitHub repository.