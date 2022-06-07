import os, requests, datetime, json


class Config(object):
    def __init__(self):
        self.API_URL_PREFIX = "http://logos.sch.ac.kr:30040"

    def ConfigObj(self):
        return self.API_URL_PREFIX


class User:
    def __init__(self):
        self.URL_PREFIX = Config().ConfigObj()
        self.URL_PREFIX_TYPE = {
            "GET": "/api/users/",
            "POST": "/api/users"
        }
        self.REQUEST_OBJ = requests
        self.RESPONSE_OBJ = None
        self.REQUEST_HEADER = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def UserRegister(self, data: dict) -> dict:
        """

        :param data: The type of "data" variable is dictionary and must contain values for the "UserName" and "UserAccountPW" keys.
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.post(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["POST"], headers=self.REQUEST_HEADER, data=json.dumps(data)
            )
            print(self.RESPONSE_OBJ.json())

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"]}

        except Exception as e:
            return {"status": 500, "message": e}

    def UserSignIn(self, uname: str, upw: str) -> dict:
        """

        :param uname:
        :param upw:
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"] + f"{uname}/{upw}", headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}

    def UserGetInformation(self, key: str) -> dict:
        """

        :param key:
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"] + key, headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}


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

    def MessageGetAllDataForChatroom(self, key: str) -> dict:
        """

        :param key:
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"] + key, headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}

    def MessageGetUserForChatroom(self, key_chat: str, key_user: str) -> dict:
        """

        :param key_chat:
        :param key_user:
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"] + f"{key_chat}/{key_user}", headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}


class ChatRoom:
    def __init__(self):
        self.URL_PREFIX = Config().ConfigObj()
        self.URL_PREFIX_TYPE = {
            "GET": "/api/chat/room",
            "POST": "/api/chat/room",
            "PATCH": "/api/chat/room/"
        }
        self.REQUEST_OBJ = requests
        self.RESPONSE_OBJ = None
        self.REQUEST_HEADER = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def ChatRoomAdd(self, data: dict) -> dict:
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

    def ChatRoomAddUser(self, key: str, data: dict) -> dict:
        """

        :param key:
        :param data: The type of "data" variable is dictionary and must contain values for the "UserName" and "UserAccountPW" keys.
        :return:

        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.patch(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["PATCH"] + key, headers=self.REQUEST_HEADER, data=json.dumps(data)
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"]}

        except Exception as e:
            return {"status": 500, "message": e}

    def ChatRoomGetAllData(self) -> dict:
        """

        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"], headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}

    def ChatRoomGetUserData(self, key_user: str, uname: str) -> dict:
        """

        :param key_user:
        :param uname:
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"] + f"/{key_user}/{uname}", headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}

    def ChatRoomGetData(self, key_chat: str) -> dict:
        """

        :param key_chat:
        :return:
        """
        try:
            self.RESPONSE_OBJ = self.REQUEST_OBJ.get(
                url=self.URL_PREFIX + self.URL_PREFIX_TYPE["GET"] + f"/{key_chat}", headers=self.REQUEST_HEADER
            )

            return {"status": self.RESPONSE_OBJ.json()["status"], "message": self.RESPONSE_OBJ.json()["message"], "data": self.RESPONSE_OBJ.json()["data"]}

        except Exception as e:
            return {"status": 500, "message": e}