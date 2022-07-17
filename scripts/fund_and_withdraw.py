from brownie import FundMe
from scripts.helpful_scripts import getaccount


def fund():
    fund_me = FundMe[-1]
    account = getaccount()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"Current entry fee is {entrance_fee}")
    fund_me.fund({"from": account, "value": entrance_fee})


def main():
    fund()
