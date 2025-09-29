"""
This script backs up Zotero entries in a project in this repository.
"""

import os
import json
import requests
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Load API credentials from environment variables
API_KEY = os.getenv("ZOTERO_KEY")
API_USER = os.getenv("ZOTERO_USER")
GROUP_ID = os.getenv("ZOTERO_GROUP")

HEADERS = {"Authorization": f"Bearer {API_KEY}"}
PARAMS = {"v": 3, "format": "json"}

# Base URL for group library
base_url = f"https://api.zotero.org/groups/{GROUP_ID}/items"


# Function to save JSON data to file
def save_json(item, folder="data"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    item_key = item.get("key", "unknown")
    filename = f"{folder}/{item_key}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=2)

    logging.debug("Saved item %s to %s", item_key, filename)


# Function to fetch items with pagination
def fetch_items():
    logging.info("Starting to fetch items from Zotero group %s", GROUP_ID)
    start = 0
    limit = 100
    while True:
        params = {"start": start, **PARAMS}

        try:
            response = requests.get(
                base_url, headers=HEADERS, params=params, timeout=10
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data at position {start}: {e}")
            break

        items = response.json()
        if not items:
            break

        for item in items:
            try:
                save_json(item)
            except Exception as e:
                print(f'Error saving item {item.get("key")} : {e}')

        start += limit

    logging.info("Finished backing up.")


if __name__ == "__main__":
    if not API_KEY or not GROUP_ID:
        print(
            "Missing required environment variables: ZOTERO_API_KEY and ZOTERO_GROUP_ID"
        )
    else:
        fetch_items()
