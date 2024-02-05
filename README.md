<h1 align="center">Telegram User Bot for Suvvy AI</h1>

<div align="center">
   
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/suvvyai/telegram-user-bot/release-package.yml)
[![Packaged with Poetry](https://img.shields.io/badge/packaging-poetry-cyan)](https://python-poetry.org/)
[![Uses Python 3.11](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Formatted with: isort](https://img.shields.io/badge/formatted%20with-isort-blue.svg)](https://github.com/psf/black)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

</div>

## About

The `telegram-user-bot` is a versatile and user-friendly integration tool designed for Suvvy AI, enabling seamless interaction between Telegram and Suvvy AI. It stands out for its ease of use, customizability, and the ability to streamline communication workflows efficiently.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose
- Basic understanding of Telegram user-bots and Docker Compose.

## Installation using Docker Compose

Use Docker Compose for a quick and straightforward setup:

1. Create a Dotenv File: Refer to the Configuration section to create a `.env` file with a Suvvy AI API key.
2. Create a Pyrogram Session: Use [barabum0/pyroauth](https://github.com/barabum0/pyroauth) to create a session file named `client.session`.
3. Download `docker-compose.yml` File:
   - With wget:
     ```bash
     wget https://raw.githubusercontent.com/suvvyai/telegram-user-bot/main/docker-compose.yml
     ```
   - Manually: [docker-compose.yml](https://github.com/suvvyai/telegram-user-bot/blob/main/docker-compose.yml)
4. Start the Service:
   ```bash
   docker-compose up -d  # or docker compose up -d
   ```

## Configuration

Create and customize your `.env`:
```bash
wget https://github.com/suvvyai/telegram-user-bot/blob/main/.env.example -O .env
nano .env
```

```shell
SESSION_NAME=client
SUVVY_API_KEY=<Your Suvvy AI API key goes here>
TIMEOUTS__BEFORE_READ_SECONDS=0
TIMEOUTS__BEFORE_ANSWER_SECONDS=0
```

## Troubleshooting

If you encounter issues, open an issue in the [GitHub repository](https://github.com/suvvyai/telegram-user-bot/issues).

## Contributing

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is under the MIT License - see the [LICENSE](https://github.com/suvvyai/telegram-user-bot/blob/main/LICENSE) file for details.

## Contact

For queries or suggestions, feel free to open an issue in the [GitHub repository](https://github.com/suvvyai/telegram-user-bot/issues).
