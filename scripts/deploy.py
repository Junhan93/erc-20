from brownie import accounts, config, TokenERC20

initial_supply = 100000000000000000000  # 100
token_name = "TOKEN"
token_symbol = "TKN"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}, publish_source=True
    )
# once we run brownie run scripts/deploy.py, we go back to see ganache with whole bunch of calls were made
# and one will show deployed at: 0x...address


# brownie run scripts/deploy.py --network kovan
# cant work ValueError: unable to expand env variable in host setting

# publish_source = true, contract automatically verified on chain

# etherscan token needed
