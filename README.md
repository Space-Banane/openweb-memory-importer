# Open Web UI Memory Importer
Import an array of strings into your Open Web UI instance through its API.

## Description
A simple Python script to import memories into Open Web UI through its API. This tool allows batch importing of string arrays as individual memories.

## Features
- Batch import of memories
- Rate-limited requests (0.4s delay between imports)
- Simple API integration
- JSON response handling

## Usage
1. Replace the `user_info` array with your desired memory strings
2. Set your authorization token in the headers
3. Run the script to import memories

## Requirements
- Python 3.9+ (Probably works with older versions, haven't tested yet)
- `requests` library
- Running Open Web UI instance

## Note
Ensure your Open Web UI is running on `localhost:3000` or modify the URL accordingly.
