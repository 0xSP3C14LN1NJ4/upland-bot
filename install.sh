#!/bin/bash

echo -e "Setting environment variables...\n"
touch .env

echo "Enter your Twilio acount SID: "
read twilio_account_sid
echo "TWILIO_ACCOUNT_SID=$twilio_account_sid" >> .env

echo "Enter your Twilio auth token: "
read twilio_auth_token
echo "TWILIO_AUTH_TOKEN=$twilio_auth_token" >> .env

echo "Enter your Twilio phone number: "
read twilio_from_number
echo "TWILIO_FROM_NUMBER=$twilio_from_number" >> .env

echo "Enter your phone number: "
read twilio_to_number
echo "TWILIO_TO_NUMBER=$twilio_to_number" >> .env

echo -e "Configuration done!\nStart the bot with 'python3 main.py'"