# Python Auto-Updater

## Overview

The **Python Auto-Updater** is an open-source, Python-based solution designed to automatically fetch and update scripts
from a remote repository. This tool checks for updates in designated files, downloads the latest versions if changes are
detected, and prompts the user to restart the application to apply updates. It can be easily integrated into different
repositories, making it a versatile choice for keeping your codebase current.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Configuration](#configuration)
- [Installation & Usage](#installation--usage)
- [File Details](#file-details)
- [License](#license)
- [Contact](#contact)

## Features

- **Automated Script Updates**:  
  Checks designated files for changes against a remote repository and updates them if newer versions are available.

- **Configurable Update Sources**:  
  Allows you to set custom URLs and file paths via a centralized `config.ini` file.

- **User Notification**:  
  Displays a message box to inform users when updates have been applied and prompts for a restart.

- **Versatile Integration**:  
  Designed to be used in various projects across different repositories with minimal setup.

- **Open Source and Free**:  
  Released under the MIT License, making it free to use, modify, and distribute.

## Configuration

Before using the auto-updater, configure the settings in the `config.ini` file. Key parameters include:

- **AutoUpdate Settings**:
    - `autoupdate`: Enable or disable automatic updates (Boolean).
    - `base_url`: The base URL for fetching updates for files like `main.py` and `config.ini`.
    - `splash_base_url`: The base URL for fetching splash screen updates (if applicable).
    - `files`: A comma-separated list of files to be checked and updated.
    - `autoupdate_url`: Specific URL for updating the `autoupdate.py` file.

### Example `config.ini`:

```ini
[AutoUpdate]
autoupdate = True
base_url = https://raw.githubusercontent.com/yourusername/yourrepository/main
splash_base_url = https://raw.githubusercontent.com/kasyan1337/personal_branding/main
files = autoupdate.py, splash.py, main.py, config.ini
autoupdate_url = https://raw.githubusercontent.com/kasyan1337/autoupdate/main/autoupdate.py
```

## Installation \& Usage

1. Ensure Python 3.7 or later is installed on your system.
2. Clone the repository:  
   `git clone <repository_url>`
3. Navigate to the project directory:  
   `cd <project_directory>`
4. Install dependencies:  
   `pip install -r requirements.txt`  
   _Required packages:_ `tkinter` (bundled with Python), `configparser`, `Pillow` (if using additional image features),
   and standard libraries.
5. Configure the Auto-Updater:  
   Update `config.ini` with your desired settings (refer to the Configuration section).
6. Run the Auto-Updater:  
   `python autoupdate.py`  
   The script checks for updates based on `config.ini`. If updates are found, they are downloaded and the user is
   prompted to restart the application.

## File Details

- `autoupdate.py`: Contains the main logic for fetching and updating files.
- `config.ini`: Central configuration file for update settings.
- Other files (e.g., `main.py` and `splash.py`) are managed similarly.

## License

This project is open source and released under the MIT License; you are free to use, modify, and distribute it in
accordance with the license terms.

## Contact

For support or inquiries, contact Kasim Janci at kasim.janci98@gmail.com.