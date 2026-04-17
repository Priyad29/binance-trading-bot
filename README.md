# Binance Trading Bot

## Overview
This project is a Python-based command-line application that allows users to place BUY and SELL orders on the Binance Testnet using API integration.

The application demonstrates basic trading operations along with structured code organization, input validation, and logging.

---

## Features

- Place MARKET and LIMIT orders  
- Supports BUY and SELL operations  
- Input validation for user inputs  
- Logging of API requests, responses, and errors  
- Modular code structure (separate files for client, orders, validation, logging)  

---

## Technologies Used

- Python  
- Binance API (python-binance library)  

---

## Setup Instructions

1. Install required dependencies:
pip install -r requirements.txt

2. Add your Binance Testnet API keys in `cli.py`:
API_KEY = "your_api_key_here"
API_SECRET = "your_secret_key_here"

3. Run the application:
python cli.py

---

## Usage

Provide the following inputs when prompted:

- Symbol (e.g., BTCUSDT)  
- Side (BUY or SELL)  
- Order Type (MARKET or LIMIT)  
- Quantity  
- Price (only for LIMIT orders)  

---

## Example

Input:
BTCUSDT  
BUY  
MARKET  
0.001  

Output:
Order placed successfully  
Order ID: XXXXX  
Status: FILLED  

---

## Logging

All API requests, responses, and errors are logged in a file named:
trading.log

---

## Notes

- This project uses Binance Testnet (no real trading involved)  
- API keys must be added manually before running  
- API keys are not included in this submission for security reasons  
