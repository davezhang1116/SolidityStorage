import json
from web3 import Web3
from dataclasses import dataclass
from typing import Optional

@dataclass
class storeData:
    
    _HTTP:str
    _abi:list
    _chainID:int
    _contractAddress:str
    _privateKey:str= None
    _index:int = None
    _firstName:str = None
    _middleNameInitial:str = None
    _lastName:str = None
    _yearBorn:int = None
    _gasPrice:int = None

    def __init__(self,_abi,_chainID,_HTTP,_contractAddress,_privateKey= None,_index= None,_firstName= None,_middleNameInitial= None,_lastName= None,_yearBorn= None,_gasPrice=None):
        self.privateKey=_privateKey
        self.abi=_abi
        self.contractAddress=_contractAddress
        self.HTTP=_HTTP
        self.chainID=_chainID
        self.index=_index
        self.firstName=_firstName
        self.middleNameInitial=_middleNameInitial
        self.lastName=_lastName
        self.yearBorn=_yearBorn
        if _gasPrice:
            self.gasPrice=_gasPrice
        else:
            self.gasPrice=3


    def store(self):
        w3 = Web3(Web3.HTTPProvider(self.HTTP))
        address = w3.eth.account.from_key(self.privateKey).address
        nonce = w3.eth.getTransactionCount(address)
        storage = w3.eth.contract(address=self.contractAddress, abi=self.abi)
        store_transaction = storage.functions.storeData(self.index, self.firstName, self.middleNameInitial, self.lastName, self.yearBorn).buildTransaction(
            {
            "chainId":self.chainID,
            "from":address,
            "gasPrice": w3.toWei(self.gasPrice, 'gwei'),
            "nonce":nonce
        }
        )
        signed_tx = w3.eth.account.sign_transaction(store_transaction, private_key=self.privateKey)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print("success")
    
    def getCount(self):
        w3 = Web3(Web3.HTTPProvider(self.HTTP))
        storage = w3.eth.contract(address=self.contractAddress, abi=self.abi)
        return storage.functions.retrieveCount().call()
    def getTotal(self):
        w3 = Web3(Web3.HTTPProvider(self.HTTP))
        storage = w3.eth.contract(address=self.contractAddress, abi=self.abi)
        return storage.functions.retrieveTotal().call()
    def removeData(self):
        w3 = Web3(Web3.HTTPProvider(self.HTTP))
        storage = w3.eth.contract(address=self.contractAddress, abi=self.abi)
        address = w3.eth.account.from_key(self.privateKey).address
        nonce = w3.eth.getTransactionCount(address)
        store_transaction = storage.functions.removeData(self.index).buildTransaction(
            {
            "chainId":self.chainID,
            "from":address,
            "gasPrice": w3.toWei(self.gasPrice, 'gwei'),
            "nonce":nonce
        }
        )
        signed_tx = w3.eth.account.sign_transaction(store_transaction, private_key=self.privateKey)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print("success")
    def retrieveData(self):
        w3 = Web3(Web3.HTTPProvider(self.HTTP))
        storage = w3.eth.contract(address=self.contractAddress, abi=self.abi)
        return storage.functions.retrieveData(self.index).call()
    def retrieveStatus(self):
        w3 = Web3(Web3.HTTPProvider(self.HTTP))
        storage = w3.eth.contract(address=self.contractAddress, abi=self.abi)
        return storage.functions.retrieveStatus(self.index).call()


