
from storeData import storeData

private_key=""
contract_address="0xA0dbaaB131CAC88908A8145DEc8D6D84b760ecB5"
abi=[{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'inputs': [], 'name': 'count', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'people', 'outputs': [{'internalType': 'uint256', 'name': 'index', 'type': 'uint256'}, {'internalType': 'string', 'name': 'firstName', 'type': 'string'}, {'internalType': 'string', 'name': 'middleNameInitial', 'type': 'string'}, {'internalType': 'string', 'name': 'lastName', 'type': 'string'}, {'internalType': 'uint16', 'name': 'yearBorn', 'type': 'uint16'}, {'internalType': 'bool', 'name': 'status', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_index', 'type': 'uint256'}], 'name': 'removeData', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'retrieveCount', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_index', 'type': 'uint256'}], 'name': 'retrieveData', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}, {'internalType': 'string', 'name': '', 'type': 'string'}, {'internalType': 'string', 'name': '', 'type': 'string'}, {'internalType': 'string', 'name': '', 'type': 'string'}, {'internalType': 'uint16', 'name': '', 'type': 'uint16'}, {'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_index', 'type': 'uint256'}], 'name': 'retrieveStatus', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'retrieveTotal', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_index', 'type': 'uint256'}, {'internalType': 'string', 'name': '_firstName', 'type': 'string'}, {'internalType': 'string', 'name': '_middleNameInitial', 'type': 'string'}, {'internalType': 'string', 'name': '_lastName', 'type': 'string'}, {'internalType': 'uint16', 'name': '_yearBorn', 'type': 'uint16'}], 'name': 'storeData', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'total', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}]
chain_id=4
HTTPProvider="https://rinkeby.infura.io/v3/9590b306ed68414293fa9f5605096986"
firstName="John1"
middleNameInitial="K1"
lastName="Doe1"
yearBorn=20001
index=2

print(
storeData(
    _privateKey = private_key,
    _contractAddress = contract_address,
    _HTTP = HTTPProvider,
    _abi=abi,
    _chainID=chain_id,
    _index=index,
    _firstName=firstName,
    _middleNameInitial=middleNameInitial,
    _lastName=lastName,
    _yearBorn=yearBorn).store())

print(
storeData(
    _abi=abi,
    _HTTP = HTTPProvider,
    _contractAddress = contract_address,
    _index=index,
    _chainID=chain_id
).retrieveData()
)


storeData(
    _privateKey = private_key,
    _contractAddress = contract_address,
    _HTTP = HTTPProvider,
    _abi=abi,
    _chainID=chain_id,
    _index=index).removeData()

print(storeData(
    _contractAddress = contract_address,
    _HTTP = HTTPProvider,
    _abi=abi,
    _chainID=chain_id).getTotal())

print(storeData(
    _contractAddress = contract_address,
    _HTTP = HTTPProvider,
    _abi=abi,
    _chainID=chain_id).getCount())

print(storeData(
    _contractAddress = contract_address,
    _HTTP = HTTPProvider,
    _abi=abi,
    _chainID=chain_id,
    _index=index,).retrieveStatus())


