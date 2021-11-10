from brownie import accounts, config, EasyToken

initial_supply = 100000000000000000000  # 100
token_name = "TOKEN"
token_symbol = "TKN"

def main():
    account = accounts[0]
    erc20 = EasyToken.deploy(initial_supply, {"from": account})
# deploy to ganache instance using brownie run scripts/deploy_ez_token
