# Zotero Group Backup

This repository contains a Python script designed to back up all records from a specified Zotero group library by fetching them via the Zotero API and saving each item as an individual JSON file.

## Purpose

To provide a reliable way to archive Zotero group data periodically (e.g., nightly), ensuring data safety and easy restoration by maintaining local JSON copies of all group items.

## Setup

1. Set the following environment variables:
   - `ZOTERO_KEY`: Your Zotero API key.
   - `ZOTERO_USER`: Your Zotero API user.
   - `ZOTERO_GROUP`: The ID of the Zotero group to back up.

2. Install dependencies

## Usage

Run the backup script: `python archive_zotero_entries.py`

The script creates a `data` folder (if not existing) and stores the JSON files inside.

