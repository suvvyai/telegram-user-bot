# Telegram User Bot for Suvvy AI
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/suvvyai/telegram-user-bot/release-package.yml)
[![Packaged with Poetry](https://img.shields.io/badge/packaging-poetry-cyan)](https://python-poetry.org/)
[![Uses Python 3.11](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)

## About
The `telegram-user-bot` is a versatile and user-friendly integration tool designed for Suvvy AI, enabling seamless interaction between Telegram and Suvvy AI. It stands out for its ease of use, customizability, and the ability to streamline communication workflows efficiently.

## Prerequisites
Before you begin, ensure you have the following installed:
- Docker
- Docker Compose
- Basic understanding of Telegram bots and Docker Compose

## Installation using Docker Compose
Use Docker Compose for a quick and straightforward setup:

1. **Create a Config File**: 
   Refer to the [Configuration](#configuration) section to create a `config.json` file with a Suvvy AI API key.

2. **Create a Pyrogram Session**: 
   Use [barabum0/pyroauth](https://github.com/barabum0/pyroauth) to create a session file named `client.session`.

3. **Download `docker-compose.yml` File**: 
   - With wget:
     ```shell
     wget https://github.com/suvvyai/telegram-user-bot/blob/main/docker-compose.yml
     ```
   - Manually:
     [docker-compose.yml](docker-compose.yml)

4. **Start the Service**:
   ```shell
   docker-compose up -d  # or docker compose up -d
   ```

## Configuration
Create and customize your `config.json`:
```shell
wget https://github.com/suvvyai/telegram-user-bot/blob/main/config.example.json -O config.json
nano config.json
```
```json
{
  "session_name": "client",
  "suvvy_api_key": "<Your Suvvy AI API Key>",
  "timeouts": {
    "before_read_seconds": 0,
    "before_answer_seconds": 0
  }
}
```
- **suvvy_api_key**: Obtain this from [Suvvy AI](https://home.suvvy.ai).

## Contributing
We welcome contributions! Here's how you can help:
- **Fork the Repository**: Make your changes in a fork.
- **Follow the Coding Standards**: Ensure your code adheres to the standards used throughout the existing codebase.
- **Submit a Pull Request**: We'll review your changes and merge them if they enhance the project.

## Troubleshooting
If you encounter issues, open an issue in the GitHub repository.

## License
This project is under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For queries or suggestions, feel free to open an issue in the [GitHub repository](https://github.com/suvvyai/telegram-user-bot/issues).