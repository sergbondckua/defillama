# DeFiLlama Data Parser

This Python script parses specific data from the DeFiLlama website at specified intervals, with the option to use a proxy. The retrieved data is saved in a JSON file in the output_files directory.


## Features
* Scrapes data from the DeFiLlama website.
* Uses the selenium library for web scraping.
* Schedules the scraping job at intervals specified in config.py using apscheduler.
* Supports proxy usage.
* Saves the scraped data as a JSON file.

## Requirements
* Python 3
* selenium library
* apscheduler library
 

## Installation

1. Clone the repository to your local machine:
`git clone https://github.com/sergbondckua/defillama.git` 
2. Navigate to the project directory:
- `cd defillama`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

3. Open `config.py` file and adjust the following parameters as needed:
- `INTERVAL_MINUTES`: Interval in minutes between each data parsing.
- To use a proxy, specify the settings `X.X.X.X:PORT` in `USE_PROXY`, otherwise leave it as is.

## Usage

To run the script, execute the following command:
`python main.py`