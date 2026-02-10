# telegram-bot-killer

## Description

This is a Python script designed to perform load testing on a Telegram bot by sending a high volume of messages to random chat IDs. It uses multi-threading to simulate concurrent requests and adjusts the sending rate based on success/failure feedback to avoid overwhelming the API.

**Warning:** This tool is intended for testing purposes only, such as evaluating bot performance under load. Misuse may violate Telegram's terms of service.

## Requirements

- Python 3.x
- No external dependencies (uses standard library modules)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Boburbro/telegram-bot-killer.git
   cd telegram-bot-killer
   ```

2. Ensure Python 3 is installed on your system.

## Usage

Run the script from the command line with your Telegram bot token:

```bash
python killer.py --token YOUR_BOT_TOKEN
```

Replace `YOUR_BOT_TOKEN` with your actual Telegram bot token obtained from [@BotFather](https://t.me/botfather).

### Command-Line Options

- `--token`: (Required) The Telegram bot token.

### Example

```bash
python killer.py --token 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

The script will start sending messages and display real-time statistics, such as the number of successful sends, failures, and the current target rate.

## How It Works

- The script sends messages to randomly generated chat IDs (10-digit numbers) to simulate load.
- It uses a thread pool (up to 20 workers) to send messages concurrently.
- The sending rate starts at 1000 messages per second and adjusts dynamically:
  - If failures exceed successes, the rate is halved (minimum 5).
  - Otherwise, the rate increases by 10 (maximum 20,000).
- Each message includes a unique number and a random 4-digit code.
- The loop runs indefinitely until manually stopped (Ctrl+C).

## Disclaimer

This code is provided for educational and testing purposes only. If used for malicious purposes, such as spamming or violating Telegram's API terms, the code author is not responsible for any consequences, including account bans or legal issues. Use at your own risk.