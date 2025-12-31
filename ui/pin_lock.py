import getpass

PIN_HASH = "1234"  # placeholder

def unlock_nsfw():
    pin = getpass.getpass("Enter NSFW PIN: ")
    return pin == PIN_HASH
