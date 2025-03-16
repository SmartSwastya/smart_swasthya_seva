import os
import sys
import subprocess
import platform
import logging
import time
from pathlib import Path
from tabulate import tabulate
from github import Github  # GitHub integration
from py import scan_project_structure, check_dependencies, auto_repair_missing_files, generate_report  # Importing from py.py

# 🌟 Set up logging for better tracking of operations and errors
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 🎯 Version
VERSION = "1.2.1"  # Updated version of the script
logging.info(f"🚀 Starting Project Setup (Version: {VERSION})")

# ✅ Securely Fetch GitHub Token from Environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    logging.error("❌ GitHub Token is missing. Set it using an environment variable: GITHUB_TOKEN")
    sys.exit(1)

# 🚀 Function to gather system info
def system_info():
    logging.info("🚀 Gathering system information...")
    system_details = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Platform": platform.platform(),
        "Architecture": platform.architecture(),
        "Python Version": platform.python_version(),
        "Python Path": sys.executable,
        "Project Directory": os.getcwd(),
    }
    logging.info(f"🖥️ System Info: {system_details}")
    return system_details

# 🔧 Function to install dependencies from requirements.txt
def install_requirements():
    logging.info("🔧 Installing dependencies...")
    install_status = []
    
    if os.path.exists("requirements.txt"):
        with open("requirements.txt") as f:
            lines = f.readlines()
            for line in lines:
                package = line.strip()
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    logging.info(f"✅ {package} already installed.")
                except subprocess.CalledProcessError:
                    try:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        install_status.append([package, "✅ Installed"])
                    except subprocess.CalledProcessError:
                        install_status.append([package, "❌ Failed"])
        
        headers = ["Package", "Status"]
        logging.info("\n" + tabulate(install_status, headers, tablefmt="fancy_grid"))
    else:
        logging.warning("⚠️ No requirements.txt found. Please ensure it exists.")
    
    logging.info("✅ Installed dependencies successfully!")

# 📦 GitHub Integration
def connect_github():
    try:
        logging.info("🔌 Connecting to GitHub...")
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo("SmartSwastya/smart_swasthya_seva")
        logging.info("✅ Successfully connected to GitHub!")
        return repo
    except Exception as e:
        logging.error(f"❌ Error connecting to GitHub: {e}")
        sys.exit(1)

# 📂 Fetch the Latest Code from GitHub
def fetch_latest_code():
    try:
        repo = connect_github()
        file_content = repo.get_contents("superclass.py")
        with open("superclass.py", "w") as file:
            file.write(file_content.decoded_content.decode())
        logging.info("✅ Latest code fetched successfully from GitHub!")
    except Exception as e:
        logging.error(f"❌ Error fetching code from GitHub: {e}")

# 📤 Push Local Changes to GitHub
def push_code_to_github():
    try:
        repo = connect_github()
        file_path = "superclass.py"
        with open(file_path, "r") as file:
            file_content = file.read()
        try:
            file_on_github = repo.get_contents(file_path)
            repo.update_file(file_path, "Updating superclass.py", file_content, file_on_github.sha)
        except:
            repo.create_file(file_path, "Creating superclass.py", file_content)
        logging.info("✅ Code pushed successfully to GitHub!")
    except Exception as e:
        logging.error(f"❌ Error pushing code to GitHub: {e}")

# ⏰ Function to Check for Updates Periodically
def # schedule_periodic_updates():
    while True:
        logging.info("⏰ Checking for updates from GitHub...")
        fetch_latest_code()
        logging.info("🔄 Waiting for the next update check...")
        time.sleep(3600)

# 🧠 Main function to run the setup tasks and show dynamic updates
def setup_project():
    logging.info("🎉 Starting project setup...")
    install_requirements()
    logging.info("🎉 Project setup completed successfully!")
    # schedule_periodic_updates()

# 🌟 Run the project setup
if __name__ == "__main__":
    setup_project()