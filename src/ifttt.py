"""
Register Amazon Dash Button events in IFTTT Maker Webhook
https://ifttt.com/maker_webhooks
"""
import json

import requests
from requests import RequestException


class Ifttt:
    def __init__(self, settings):
        self.settings = settings
        self.key_file = self.load_key()
        self.key = self.key_file["key"]

    def load_key(self):
        with open(self.settings["ifttt_key_file_name"], "r", encoding="utf-8-sig") as key_file:
            return json.loads(key_file.read())

    def press(self, summary, v1, v2, v3):
        payload = {"value1": v1, "value2": v2, "value3": v3}
        # todo urlencode event string
        try:
            url = "https://maker.ifttt.com/trigger/{event}/with/key/{key}".format(
                event=summary, key=self.key
            )
            result = requests.post(
                url, data=json.dumps(payload), headers={"content-type": "application/json"}
            )
            if result.status_code != 200:
                print("*" * 10, "IFTTT error:\n", url, "\n", result)
        except RequestException as e:
            print("*" * 10, "IFTTT request fail:\n", url, "\n", e)


if __name__ == "__main__":  # pragma: no cover
    from amazon_dash import load_settings

    settings = load_settings()
    ifttt = Ifttt(settings)
    ifttt.press("white_amazon_dash", "1", "2", "3")
