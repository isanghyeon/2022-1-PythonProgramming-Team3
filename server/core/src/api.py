import os, requests, datetime, json


class Config(object):
    def __init__(self):
        self.API_URL_PREFIX = "http://localhost:30000"

    def ConfigObj(self):
        return self.API_URL_PREFIX


class Message:
    def __init__(self):
        self.URL_PREFIX = Config().ConfigObj()
        self.URL_PREFIX_TYPE = {
            "GET": "/api/chat/msg/",
            "POST": "/api/chat/msg"
        }
        self.REQUEST_OBJ = requests
        self.RESPONSE_OBJ = None
        self.REQUEST_HEADER = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def MessageAdd(self, data: dict) -> dict:
        """

        :param data: The type of "data" variable is dictionary and must contain values for the "UserName" and "UserAccountPW" keys.
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.post(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["POST"], headers=self.REQUEST_HEADER, data=json.dumps(data)
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"]}

        except Exception as e:
            return {"status": 500, "message": e}
