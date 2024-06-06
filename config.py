import logging

from pathlib import Path

from environs import Env
from fake_useragent import UserAgent


# Fake user agent
ua = UserAgent()

# Read environment variables
env = Env()
env.read_env()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Base URL
BASE_URL = "https://defillama.com"

# Chrome driver options
option_arguments = [
    "--headless=new",
    "--hide-scrollbars",
    "start-maximized",
    "--no-sandbox",
    "--disable-blink-features=AutomationControlled",
    "disable-popup-blocking",
    f"--user-agent={ua.firefox}",
]

# Parsing start interval in minutes
INTERVAL_MINUTES = 5

# Proxy for webdriver
USE_PROXY = ""  # X.X.X.X:PORT
