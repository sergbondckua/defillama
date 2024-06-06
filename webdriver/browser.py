import os

from selenium import webdriver
from selenium.common import WebDriverException

import config


class BrowserManager:
    """A context manager for managing a Selenium web browser instance."""

    def __init__(self):
        self.options_arguments = config.option_arguments
        self.options = self._driver_options()
        self.browser = None

    def __enter__(self):
        self.start_browser()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_browser()

    def _driver_options(self):
        """Configure ChromeOptions for the webdriver."""
        options = webdriver.ChromeOptions()
        self._add_options_arguments(options)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return options

    def _add_options_arguments(self, options: webdriver.ChromeOptions):
        """Add arguments to the ChromeOptions"""
        for argument in self.options_arguments:
            options.add_argument(argument)
        if config.USE_PROXY:
            options.add_argument(f"--proxy-server={config.USE_PROXY}")

    def start_browser(self):
        """Start the web driver (remote or local)."""
        try:
            self.browser = webdriver.Chrome(options=self.options)
            self.browser.set_window_size(1366, 15650)
            # Substitution of `navigator.webdriver`
            self.browser.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {
                    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                """
                },
            )
        except WebDriverException as error:
            config.logger.error("Error starting the web browser: %s", str(error))
            raise error
        return self.browser

    def close_browser(self):
        """Close the web browser."""
        try:
            if self.browser:
                self.browser.quit()
                config.logger.info("Browser closed")
        except WebDriverException as e:
            config.logger.error("Error closing the web browser: %s", str(e))
