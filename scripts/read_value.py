from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1] # -1 for latest deployment 
    print(simple_storage)
    # go take the index thats one less than the length
    # ABI
    # Address
    print(simple_storage.reterieve())


def main():
    read_contract()
