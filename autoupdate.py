import os, ssl, sys, configparser, logging, urllib.request
from tkinter import messagebox


# DEFINE update_scripts to automatically fetch and update files
def update_scripts():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_dir = os.path.join(base_dir, "src")
    config = configparser.ConfigParser()
    config.read(os.path.join(base_dir, "config.ini"))
    auto_update_enabled = config.getboolean("AutoUpdate", "autoupdate", fallback=True)
    if not auto_update_enabled:
        # logging.info("Auto-update is disabled in config.ini.") #DEBUG
        return False
    base_url = config.get("AutoUpdate", "base_url")
    splash_base_url = config.get(
        "AutoUpdate",
        "splash_base_url",
        fallback="https://raw.githubusercontent.com/kasyan1337/personal_branding/main",
    )
    files_str = config.get("AutoUpdate", "files")
    files_list = [f.strip() for f in files_str.split(",")]
    RAW_FILES = {}
    for f in files_list:
        if f == "autoupdate.py":
            RAW_FILES[f] = (
                f"{config.get('AutoUpdate', 'autoupdate_url').rstrip('/')}/{f}"
            )
        elif f == "splash.py":
            RAW_FILES[f] = f"{splash_base_url}/{f}"
        elif f in ("main.py", "config.ini"):
            RAW_FILES[f] = f"{base_url}/{f}"
        else:
            RAW_FILES[f] = f"{base_url}/src/{f}"
    ssl_context = ssl._create_unverified_context()
    updated = False
    for file_name, raw_url in RAW_FILES.items():
        local_file_path = (
            os.path.join(base_dir, file_name)
            if file_name in ("main.py", "config.ini")
            else os.path.join(script_dir, file_name)
        )
        # logging.info("Checking for updates for %s from %s", file_name, raw_url) #DEBUG
        try:
            with urllib.request.urlopen(
                raw_url, context=ssl_context, timeout=10
            ) as response:
                latest_code = response.read().decode("utf-8")
        except Exception as e:
            # logging.error("Failed to fetch %s: %s", file_name, e) #DEBUG
            continue
        if os.path.exists(local_file_path):
            with open(local_file_path, "r", encoding="utf-8") as local_file:
                local_code = local_file.read()
        else:
            local_code = ""
        if local_code != latest_code:
            with open(local_file_path, "w", encoding="utf-8") as local_file:
                local_file.write(latest_code)
            # logging.info("%s was updated.", file_name) #DEBUG
            updated = True
        else:
            logging.info("%s is already up to date.", file_name)
    if updated:
        messagebox.showinfo(
            "Update",
            "Scripts were updated. Please restart the application to apply the changes.",
        )
        sys.exit(0)
    else:
        logging.info("All scripts are up to date.")
        return False
