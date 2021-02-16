from constants import *

import subprocess
import json
import os
from dotenv import load_dotenv

from web3 import Web3
from eth_account import Account
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

# Set the mnemonic as environmental variable
load_dotenv()
mnemonic = os.getenv('MNEMONIC', 'young rifle express flag palm roast report potato tone oven deal play')

# Connect to PoA algorithm
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

# function to get information of wallets
def derive_wallets(mnemonic, coin, numderive):
    
    # run the command to fetch wallet information
    command = f'php derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{numderive}" --cols=path,address,privkey,pubkey,pubkeyhash,xprv,xpub --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    
    # create lists to hold wallet information, which are later nested in a dictionary
    if coin == ETH:
        return list(keys)
    elif coin == BTCTEST:
        return list(keys)

# function to convert the privkey string in a child key to an account object
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# function to create the raw, unsigned transaction that contains all metadata needed to transact
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas({
                                          'from': account.address,
                                          'to': to,
                                          'value': amount
                                          })
        return {
                'to': to,
                'from': account.address,
                'value': amount,
                'gas': gasEstimate,
                'gasPrice':w3.eth.gasPrice,
                'nonce': w3.eth.getTransactionCount(account.address)
                }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

# function to sign the transaction and then send it to the designated network
def send_tx(coin, account, to, amount):
    raw_tx = create_tx(coin, account, to, amount)
    sign_tx = account.sign_transaction(raw_tx)
    if coin == ETH:
        send_to_blockchain = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
        return send_to_blockchain
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(sign_tx)

# create a dictionary holding the information of 3 wallets
coins = {'btc-test': derive_wallets(mnemonic, BTCTEST, 3),
         'eth': derive_wallets(mnemonic, ETH, 3)}
print(coins)


# TestnetBitcoin transaction
# send test BTC from the first child address to the second child address
btctest_sender_account = priv_key_to_account(BTCTEST,coins['btc-test'][0]['privkey'])
btctest_recipient_address = coins['btc-test'][1]['address']

send_tx(BTCTEST, btctest_sender_account, btctest_recipient_address, .0000001)

# Test ETH transaction
# send test ETH from the first child address to the second child address
eth_sender_account = priv_key_to_account(ETH, coins['eth'][0]['privkey'])
eth_recipient_address = coins['eth'][1]['address']

send_tx(ETH, eth_sender_account, eth_recipient_address, 3000000000000)



