import csv

import requests

from app.loggers.loggers import get_custom_logger


def read_csv_file(url):
    logger = get_custom_logger(__name__)
    logger.info(f"start reading csv file from {url}")
    with requests.get(url) as data:
        csv_reader = csv.DictReader(data.text.splitlines())
        temp_weight = []
        temp_height = []

        for row in csv_reader:
            temp_weight.append(float(row['Weight(Pounds)']) * 0.453592)
            temp_height.append(float(row['Height(Inches)']) * 2.54)

        print(f"Average Height (cm): {sum(temp_height) / len(temp_height):.2f}")
        print(f"Average Weight (kg): {sum(temp_weight) / len(temp_weight):.2f}")
