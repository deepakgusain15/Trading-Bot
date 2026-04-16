# Binance Futures Trading Bot

A simple Python-based trading bot that interacts with Binance Futures Testnet to place Market and Limit orders using a clean CLI interface.

---

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY & SELL
- Command Line Interface (CLI)
- Input validation
- Logging of API requests & responses
- Error handling (API, network, invalid input)

---

## Tech Stack

- Python 3
- python-binance
- argparse
- logging

---

## Setup Instructions

1. Clone the repository:

git clone https://github.com/deepakgusain15/trading-bot.git
cd trading-bot

2. Install dependencies:

pip install -r requirements.txt

3. Create a `.env` file in root directory and add:

API_KEY=your_api_key
API_SECRET=your_secret_key

---

## Usage

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 75000

---

## Sample Output

Order Summary  
Symbol: BTCUSDT  
Side: BUY  
Type: MARKET  
Quantity: 0.001  

Response  
Order ID: 12345678  
Status: NEW  
Executed Qty: 0.001  

---

##  Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── __init__.py
│
├── cli.py
├── requirements.txt
├── README.md

---

##  Notes

- This project uses Binance Futures Testnet (no real money involved)
- Do NOT share your API keys publicly
- `.env` file is excluded using `.gitignore`

---

##  Future Improvements

- Add Stop-Limit or OCO orders
- Interactive CLI input
- Basic UI dashboard

---

## Author

Developed by Deepak Gusain