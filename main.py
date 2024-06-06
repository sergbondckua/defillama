from apscheduler.schedulers.blocking import BlockingScheduler

import config
from webdriver.parse import DataSeeker


def main():
    chains = DataSeeker()
    chains.retrieve_chains_data()


def schedule_job():
    scheduler = BlockingScheduler()
    scheduler.add_job(main, "interval", minutes=config.INTERVAL_MINUTES)
    scheduler.start()


if __name__ == "__main__":
    schedule_job()
