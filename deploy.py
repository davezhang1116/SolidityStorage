import json
from web3 import Web3
from solcx import compile_standard, install_solc


install_solc("0.8.0")
with open("./Storage.sol", "r") as file:
    storage = file.read()


# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Storage.sol": {"content": storage}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["Storage.sol"]["Storage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["Storage.sol"]["Storage"]["abi"]
print(abi)

w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/9590b306ed68414293fa9f5605096986"))
chain_id=4
private_key=""
address= w3.eth.account.from_key(private_key).address
Storage =  w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(address)

transaction = Storage.constructor().buildTransaction({
    "chainId":chain_id,
    "from":address,
    "nonce":nonce
})

signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("contract address:")
print(tx_receipt.contractAddress)