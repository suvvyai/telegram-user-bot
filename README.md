# Telegram User Bot for Suvvy AI

## About
The `telegram-user-bot` is an integration tool designed for Suvvy AI. This project allows seamless interaction between Telegram and Suvvy AI via user bot, providing an efficient and user-friendly platform for communication.

## Installation using Docker Compose
Alternatively, you can use Docker Compose:
1. [Create a config](#configuration) and pass a Suvvy AI API key into it.

   *(it is not required to change something else in default config besides suvvy_api_key)*

   *(config file should be named **config.json** and be in the same folder as your docker compose file.)*


2. Create a pyrogram session using [barabum0/pyroauth](https://github.com/barabum0/pyroauth)

   *(session file should be named **client.session** and be in the same folder as your docker compose file.)*


3. Create a `docker-compose.yml` file with the following content:
   ```yaml
   version: '3.8'
   services:
     telegram_user_bot:
       image: ghcr.io/suvvyai/telegram_suvvy_user_bot:latest
       volumes:
         - ./config.json:/usr/src/app/config.json
         - ./client.session:/usr/src/app/client.session  # It must be the same as "session_name" in config with .session
   ```
   
4. Run the following command:
   ```shell
   docker-compose up -d  # or docker compose up -d
   ```

## Usage
The bot can be used directly through the running Docker container. Make sure to mount your `config.json` when starting the container.

## Configuration
Create a `config.json` file in your project directory:
```shell
wget https://github.com/suvvyai/telegram-user-bot/blob/main/config.example.json -O config.json
nano config.json
```
```json
{
  "session_name": "client",
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