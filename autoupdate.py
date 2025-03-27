import os
import ssl
import sys
import urllib.request
import configparser
from tkinter import messagebox


def update_scripts():
    # Set BASE and SCRIPT directories (MNEMONIC: BASE=UP one level; SRC=child folder)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_dir = os.path.join(base_dir, 'src')

    # Read configuration from config.ini in base_dir (CONFIG details in [AutoUpdate] section)
    config = configparser.ConfigParser()
    config.read(os.path.join(base_dir, 'config.ini'))
    auto_update_enabled = config.getboolean('AutoUpdate', 'autoupdate', fallback=True)
    if not auto_update_enabled:
        print("Auto-update is disabled in config.ini.")
        return False

    base_url = config.get('AutoUpdate', 'base_url')
    splash_base_url = config.get('AutoUpdate', 'splash_base_url',
                                 fallback="https://raw.githubusercontent.com/kasyan1337/personal_branding/main")
    files_str = config.get('AutoUpdate', 'files')
    files_list = [f.strip() for f in files_str.split(',')]

    # Build RAW_FILES mapping: for splash.py use splash_base_url; for main.py and config.ini, use base_url directly; others in src/
    RAW_FILES = {}
    for f in files_list:
        if f == "splash.py":
            RAW_FILES[f] = f"{splash_base_url}/{f}"
        elif f in ("main.py", "config.ini"):
            RAW_FILES[f] = f"{base_url}/{f}"
        else:
            RAW_FILES[f] = f"{base_url}/src/{f}"

    ssl_context = ssl._create_unverified_context()
    updated = False
    for file_name, raw_url in RAW_FILES.items():
        # Determine local path: main.py and config.ini are in base_dir; other files are in script_dir
        local_file_path = os.path.join(base_dir, file_name) if file_name in ('main.py', 'config.ini') else os.path.join(
            script_dir, file_name)
        # print(f"Checking updates for the file: {file_name} from {raw_url}...")
        try:
            with urllib.request.urlopen(raw_url, context=ssl_context, timeout=10) as response:
                latest_code = response.read().decode('utf-8')
        except Exception as e:
            print(f"Failed to fetch {file_name}: {e}")
            continue

        if os.path.exists(local_file_path):
            with open(local_file_path, 'r', encoding='utf-8') as local_file:
                local_code = local_file.read()
        else:
            local_code = ''

        # ONLY update if the remote code differs (MNEMONIC: CHANGE = ONLY if DIFFERENT)
        if local_code != latest_code:
            with open(local_file_path, 'w', encoding='utf-8') as local_file:
                local_file.write(latest_code)
            print(f"{file_name} was updated.")
            updated = True
        else:
            print(f"{file_name} is already up to date.")
    if updated:
        messagebox.showinfo("Update", "Scripts were updated. Please restart the application to apply the changes.")
        sys.exit(0)
    else:
        print("All scripts are up to date.")
        return False