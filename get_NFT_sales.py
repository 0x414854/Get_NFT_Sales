import os
import requests
import json
import schedule
import time
import logging

"""
This script fetches and saves sales events from a specified OpenSea collection
to a JSON file, checking for updates and logging events.
"""

COLLECTION = 'pudgypenguins'
API_URL = f"https://api.opensea.io/api/v2/events/collection/{COLLECTION}?event_type=sale"
API_KEY = "YOUR_API_KEY"
FILE_PATH = f'./{COLLECTION}.json'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_and_save_sales():
    try:
        headers = {
            "accept": "application/json",
            "x-api-key": API_KEY
        }
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            new_sales = json.loads(response.text)['asset_events']
            
            try:
                with open(FILE_PATH, 'r') as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = {'asset_events': []}

            updated_sales = [sale for sale in new_sales if sale not in existing_data['asset_events']]

            if updated_sales:
                existing_data['asset_events'] = updated_sales + existing_data['asset_events']

                with open(FILE_PATH, 'w') as file:
                    json.dump(existing_data, file, indent=2)
                    logging.info("Data saved successfully.")
            else:
                logging.info("Existing data is already up-to-date.")
        else:
            logging.error(f"Request failed. Status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error : {str(e)}")
    except Exception as e:
        logging.error(f"An error occurred : {str(e)}")


def main():
    fetch_and_save_sales()

    schedule.every(5).minutes.do(fetch_and_save_sales)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()

