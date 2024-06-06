from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import config
from save import save_to_json
from webdriver.page_utils import PageUtils


class ChainsData(PageUtils):
    """Class to fetch table data from a webpage."""

    def __init__(self, browser: webdriver):
        super().__init__(browser)
        self.browser = browser

    @staticmethod
    def _extract_row_data(row: WebElement) -> dict:
        """Extracts data from a single table row."""

        cols = row.find_elements(By.XPATH, "./div")
        col1 = cols[0].text.split("\n")[1].strip()
        col2 = cols[1].text.strip()
        col7 = cols[6].text.strip()
        return {col1: {"protocol": col2, "tvl": col7}}

    def _extract_data(self) -> list[dict[str, dict]]:
        """Extracts data from the table."""

        source = self._wait_element((By.CLASS_NAME, "laCLKq"))
        table = source.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/div/main/div[2]/div[4]/div[2]"
        )

        # Locate all rows
        rows = table.find_elements(
            By.XPATH,
            "//*[@id='__next']/div[1]/div/main/div[2]/div[4]/div[2]/div",
        )

        # Extract data from each row
        data = [self._extract_row_data(row) for row in rows]
        config.logger.info("Processing %s rows", len(rows))

        return data

    def get_chains(self) -> None:
        """Opens the webpage, extracts table data, and saves it to a JSON file."""

        filename = "output_files/chains_data.json"
        self._open_page(config.BASE_URL + "/chains")
        data = self._extract_data()
        config.logger.info("Processing completed successfully.")
        save_to_json(data, filename)
        config.logger.info("Data saved to file: %s", filename)
        return
