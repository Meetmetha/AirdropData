import json
import time
from web3 import Web3
import requests
from eth_account import Account
from web3 import Web3
from eth_account.messages import encode_defunct
from loguru import logger
import json
f = open('wallets.json')
data = json.load(f)

def start():
    for i in data:
        try:
            check('Pass-Key-Here (i)')
        except:
            pass

def check(key):
    ts = time.time() 
    msg = f'''Greetings from Avail!

Sign this message to check your eligibility. This signature will not cost you any fees.

Timestamp: {int(ts)}'''
    msghash = encode_defunct(text=msg)
    account = Account.from_key(key)
    sign = account.sign_message(msghash)
    url = 'https://claim-api.availproject.org/check-rewards'
    sign = sign.signature.hex()
    payload = {
            'account': Web3.toChecksumAddress(account.address).lower(),
            'signedMessage': sign.lower(),
            'timestamp': int(ts),
            'type': 'ETHEREUM'
    }
    res = requests.post(url=url, json=payload)
    print(account.address,res.text)

start()
