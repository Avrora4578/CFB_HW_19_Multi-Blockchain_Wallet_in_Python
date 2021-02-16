# CFB_HW_19_Multi-Blockchain_Wallet_in_Python

## Goal: Create Multi-Blockchain Wallet in Python

The purpose of this assignment is to create wallets for multiple cryptocurrencies and test a transaction between two nodes.<br>

## Workflow

### (1) Install and Prepare Dependencies

For this project, among others, the following libraries and tools are needed.<br>
 1. hd-wallet-derive<br>
 2. bit Python Bitcoin Library<br>
 3. web3 Python Ethereum Library<br>

### (2) Set up the Directory

First, prepare the directory and files to run scripts in the code. The details of the directory and commands on Git Bash are as below. You can confirm that the Git Bash command returns addresses of child wallets that are produced by BIP39.<br>
<img width="400" alt="directory.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/directory.PNG">
<br>
<img width="900" alt="wallets_gitbash.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/wallets_gitbash.PNG">
<br>
<img width="900" alt="wallets_bip39.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/wallets_bip39.PNG">
<br>

### (3) Access Wallet Information on Python

Using the subprocess library, run the Git Bash commands above as the Python code. You can get the exactly same wallet information by running the Python file.<br>
<img width="900" alt="wallet_keys_on_python.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/wallet_keys_on_python.PNG">
<br>


### (4) Coding Functions to Transact Bitcoin and Ethereum

Now that you have the information of multiple wallets, you can send and receive the Testnet Bitcoin and Ethereum between those wallets. The code for the transaction is as follows.<br>
<img width="600" alt="functions.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/functions.PNG">
<br>

### (5) Testnet BTC Transaction

Before transacting BTC, get the Testnet BTC from Bitcoin testnet3 faucet (https://coinfaucet.eu/en/btc-testnet/). The link in the instructions did not work, so I used a different faucet.<br>
<img width="900" alt="btc_testnet_coin.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/btc_testnet_coin.PNG">
<br>
Next, call the functions just created above and send a certain amount of Testnet BTC from the first child wallet to the second child wallet. The code to call the functions and the result of the transaction are as follows. You can see that 0.000001 Testnet BTC has been sent from the first child wallet (underlined) to the second one (underlined).<br>
<img width="900" alt="btc_transaction.jpg" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/btc_transaction.jpg">
<br>

### (6) Create PoA Chain

Just like the Homework 18, create two new nodes and a genesis block based on proof of authority, initialize the nodes, and start a mining process. I only show a screenshot of the mining process below, but the whole Git Bash code for this process is available in the file titled 'Codes_GitBash.txt' in this repository. I intentionally wrote down the mnemonic and private key of the parent wallet to show the process clearly. I use this wallet and its child wallets only for the purpose of this project. <br>
<img width="500" alt="poa_mining.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/poa_mining.PNG">


### (7) Test ETH Transaction

Before testing a test ETH transactions between two child wallets, you have to send some amount of ETH to a child wallet because in the beginning child wallets are empty. To do so, access the local PoA chain on My Crypto just like in the Homework 18 and send 1000 ETH from the node1 sealing account to a child wallet. <br>
<img width="500" alt="preparation.jpg" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/preparation.jpg">
<br>
<br>
Finally, call the functions in wallet.py and send 100 ETH from the first child wallet to the second one. The code to call the functions and the result of the transaction are as follows. You can check the balances of the two wallets have been changed according to the transaction.<br>
<img width="900" alt="eth_transaction.jpg" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/eth_transaction.jpg">
<br>
<img width="300" alt="result1.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/result1.PNG">
<img width="300" alt="result2.PNG" src="https://github.com/Avrora4578/CFB_HW_19_Multi-Blockchain_Wallet_in_Python/blob/main/Screenshots/result2.PNG">






























