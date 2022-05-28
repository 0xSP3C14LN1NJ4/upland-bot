import requests
import json
import os
import time
from twilio.rest import Client
from dotenv import load_dotenv

UPX_PRICE = 3500
FIAT_PRICE = 3


def get_actions():
    url = "https://api.eosflare.io/v1/eosflare/get_actions"
    data = '{"account_name":"playuplandme", "pos":-30, "offset":-1000}'
    r = requests.post(url, data)
    return json.loads(r.text)["actions"]


def get_transactions(actions):
    transactions = []

    for action in actions:
        act = action["action_trace"]["act"]

        if act["name"] == "n2":
            transactions.append(act)

    return transactions


def check_price(transactions):
    properties = []

    for transaction in transactions:
        data = transaction["data"]
        property_id = data["a45"]
        upx_price = float(data["p11"].replace(" UPX", ""))
        fiat_price = float(data["p3"].replace(" FIAT", ""))

        if upx_price > 0 and upx_price <= UPX_PRICE:
            properties.append({"property_id": property_id, "price": str(upx_price) + " UPX"})

        if fiat_price > 0 and fiat_price <= FIAT_PRICE:
            properties.append({"property_id": property_id, "price": str(fiat_price) + " USD"})

    return properties


def send_sms(properties):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ['TWILIO_FROM_NUMBER']
    to_number = os.environ['TWILIO_TO_NUMBER']
    client = Client(account_sid, auth_token)

    text = "New property available for sale at a low price!\n"

    for property in properties:
        text += "Price: " + property["price"] + "\n"
        text += "https://play.upland.me/?prop_id=" + property["property_id"] + "\n\n" 

    message = client.messages \
        .create(
            body=text,
            from_=from_number,
            to=to_number
        )


if __name__ == "__main__":
    load_dotenv()
    while True:
        actions = get_actions()
        transactions = get_transactions(actions)
        properties = check_price(transactions)

        if properties:
            send_sms(properties)

        time.sleep(100)