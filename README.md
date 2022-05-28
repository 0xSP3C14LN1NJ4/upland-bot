# Upland Bot
An Upland bot sending an SMS when a cheap property is available for sale at a low price

**NOTE: To use this bot, you must have a Twilio account as it is used to send SMS**


## Installation and usage
- Clone this repository
```
$ git clone https://github.com/0xSP3C14LN1NJ4/upland-bot.git
```

- Move into this directory
```
$ cd upland-bot
```

- Create an account on [Twilio](https://www.twilio.com/) and take note of your account SID and auth token

- Run the install script
```
./install.sh
```

- In `main.py`, change UPX_PRICE and FIAT_PRICE to the limit you want to use for the bot

- Run the bot by running
```
$ python3 main.py
```
