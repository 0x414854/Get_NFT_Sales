![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Get NFT Sales 

## **Description**
**This Python script fetches and saves sales events from a specified OpenSea collection.**
<br>It checks for updates at regular intervals, logs the events, and saves the data to a JSON file.
<br>The script ensures new sales events are appended to the existing data and avoids duplication.


## **Features**
- **Fetch Sales Events** : Retrieves sales events from a specified OpenSea collection.
- **JSON Data Storage** : Saves sales events data to a JSON file.
- **Update Check** : Periodically checks for new sales events and updates the JSON file.
- **Logging** : Logs the status of data fetching and updates.

## **Prerequisites**
- **Python 3.x** installed on your machine
- **requests** and **schedule** libraries

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the script.

1. Clone this repository to your machine.
   
   ```bash
   git clone https://github.com/0x414854/Get_NFT_sales.git

2. Navigate to the repository directory.

   ```bash
    cd Get_NFT_sales

3. Install the required libraries.
   
    ```bash
    pip install requests schedule

## **Usage Examples**
1. Open the '**get_NFT_sales.py**' script and **replace '*YOUR_API_KEY*' with your actual OpenSea API key**.
   
2. Run the script!
   
   ```bash
   python3 get_NFT_sales.py
   
3. The script will fetch sales events from the specified OpenSea collection and save them to a JSON file.

4. It will check for updates every 5 minutes and log the status of each operation.
   
## Tree Directory

Get_NFT_Sales/
<br>├── get_NFT_sales.py
<br>├── pudgypenguins.json (example)
<br>└── README.md

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)
