
from chains import ChainsData
from webdriver.browser import BrowserManager


class DataSeeker:
    """
    The Retriever class is responsible for initializing the browser
    and retrieving data.
    """

    def __init__(self):
        self.browser = BrowserManager().start_browser()
        self.chains_data = ChainsData(self.browser)

    def retrieve_chains_data(self):
        """Retrieves chain data."""
        return self.chains_data.get_chains()
