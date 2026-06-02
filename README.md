# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified trading bot built using Python for Binance Futures Testnet (USDT-M).

It supports:

* MARKET orders
* LIMIT orders
* BUY and SELL sides
* Command-line interface (CLI)
* Logging
* Input validation
* Exception handling

---

## Project Structure

```text
trading_bot_assignment/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository_url>
cd trading_bot_assignment
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

## Running the Bot

### MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 70000
```

---

## Logging

Logs are stored in:

```text
logs/trading_bot.log
```

The bot logs:

* API requests
* API responses
* Errors

---

## Assumptions

* Binance Futures Testnet account is configured
* Valid API credentials are provided
* User provides valid trading symbol and quantity

