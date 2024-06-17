# Roblox Group Sale Notifier

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

## 🚀 Introduction

The **Roblox Group Sale Notifier** is a Python-based script that tracks sales within a Roblox group and sends notifications to a Discord webhook. This tool is perfect for Roblox game developers and group managers who want real-time updates on sales transactions.

## 📜 Features

- Tracks various types of sales including Game Passes, Private Servers, Developer Products, and Assets.
- Sends detailed notifications to a Discord webhook.
- Logs all transactions with timestamps.
- Easy to configure and run.

## 🛠️ Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Roblox-Group-Sale-Notifier.git
    cd Roblox-Group-Sale-Notifier
    ```

2. **Install the required dependencies:**

    ```bash
    pip install requests
    ```

3. **Configure the script:**

    Open the `script.py` file and update the `Stuff` class with your Roblox security cookie, group ID, and Discord webhook URL.

    ```python
    class Stuff:
        cookie = ''  # Your Roblox security cookie
        groupid = ''  # Your Roblox group ID
        webhook = ''  # Your Discord webhook URL
        timeout = 10  # Optional: Adjust timeout value
        wait = 5  # Optional: Adjust wait time
    ```

## 📄 Usage

Run the script using Python:

```bash
python script.py
```

Once the script is running, it will continuously check for new sales and send notifications to the configured Discord webhook.
📊 Notification Example
Here is what a sale notification will look like in Discord:
![Example](https://i.imgur.com/oFIZdRd.png)


🛡️ License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

💬 Contact
For support, join our Discord server.

