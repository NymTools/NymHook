# NymHook

A Discord Webhook Multi-Tool.

## Description

NymHook is a Python-based command-line tool designed to interact with Discord webhooks. It provides functionalities to send embeds, spam messages, delete webhooks, retrieve webhook information, and send files through a Discord webhook. This tool aims to simplify and enhance the use of Discord webhooks for various purposes.

## Features and Functionality

*   **Webhook Setup:** Automatically configures the webhook URL at startup.
*   **Send Embeds:** Creates and sends customized embeds with titles, descriptions, and selectable colors.
*   **Spam Webhook:** Sends multiple messages to the webhook with a specified delay (use with caution).
*   **Delete Webhook:** Permanently deletes the configured webhook.
*   **Show Webhook Info:** Retrieves and displays information about the webhook, such as name, ID, and channel ID.
*   **Send File:** Sends a local file through the webhook.
*   **Color Test:** Demonstrates available colors for embeds and provides gradient examples for console output.
*   **Cross-Platform Compatibility**: Works on both Windows and Linux/macOS.

## Technology Stack

*   Python 3.x
*   `requests` library: For making HTTP requests to the Discord API.
*   `json` library: For handling JSON data.
*   `time` library: For adding delays in spam functionality.
*   `threading` library: (Not explicitly used in the provided code, but potentially intended for future asynchronous operations).
*   `datetime` library: For handling timestamps in embeds.
*   `os` library: For clearing the screen and setting the window title.
*   `sys` library:  For writing escape sequences to set window title in Linux/macOS.
*   `shutil` library: For determining terminal size for text centering.

## Prerequisites

*   Python 3.x installed on your system.
*   `requests` library. Install it using pip:

    ```bash
    pip install requests
    ```

## Installation Instructions

1.  Clone the repository:

    ```bash
    git clone https://github.com/NymTools/NymHook.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd NymHook
    ```

3.  Install the required dependencies:

    ```bash
    pip install requests
    ```

## Usage Guide

1.  Run the `NymHook.py` script:

    ```bash
    python NymHook.py
    ```

2.  The script will prompt you to enter the webhook URL. Provide a valid Discord webhook URL.

3.  After the webhook is set up, the main menu will be displayed with the following options:

    *   `[1] Send Embed`: Create and send a custom embed. You will be prompted for the title, description, and color.
    *   `[2] Spam Webhook`: Send a message multiple times with a delay.  **Warning: Excessive spamming can lead to rate limits or webhook deletion by Discord.**
    *   `[3] Delete Webhook`:  Deletes the configured webhook.
    *   `[4] Show Webhook Info`: Displays information about the webhook.
    *   `[5] Send File`: Sends a file through the webhook. You will be prompted for the file path.
    *   `[6] Color Test`: Displays available embed colors and gradient examples.
    *   `[0] Exit`: Exits the program.

4.  Enter the number corresponding to the desired option and follow the prompts.

## API Documentation

This tool interacts with the Discord API through webhook URLs. It uses the `requests` library to send HTTP POST, GET, and DELETE requests.

*   **POST Request (Send Embed/Message/File):**
    *   Endpoint: Your webhook URL
    *   Data: JSON payload containing the embed/message content or the file to be sent.
    *   Headers: Content-Type: application/json (for JSON payloads)
*   **GET Request (Webhook Info):**
    *   Endpoint: Your webhook URL
    *   Purpose: Retrieves information about the webhook.
*   **DELETE Request (Delete Webhook):**
    *   Endpoint: Your webhook URL
    *   Purpose: Deletes the webhook.

Example of sending an embed (from the code):

```python
embed = {
    "title": title,
    "description": description,
    "color": color,
    "timestamp": datetime.utcnow().isoformat(),
    "footer": {
        "text": "NymHook v2.0"
    }
}

data = {"embeds": [embed]}

response = requests.post(self.webhook_url, json=data)
```

## Contributing Guidelines

Contributions are welcome! If you'd like to contribute to NymHook, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Test your changes thoroughly.
5.  Submit a pull request to the `main` branch.

## License Information

License not specified.

## Contact/Support Information

This project is maintained by NymTools. For support or inquiries, please open an issue on the GitHub repository: [https://github.com/NymTools/NymHook](https://github.com/NymTools/NymHook)