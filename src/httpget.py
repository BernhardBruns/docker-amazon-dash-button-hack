import json

import requests

import models


class HttpGet:
   

    def __init__(self, settings: models.Settings) -> None:
        """Init."""
        self.settings = settings

    def press(self, action_params: models.HttpGetAction) -> None:
       
              
        requests.get(action_params.path)
        print(
               'Try GET-Request for URL: ({action_params.path}) '
            )
