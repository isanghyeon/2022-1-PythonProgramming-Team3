# -*- coding: utf-8 -*-

"""
    Python Programming Project - Team 3
    ~~~~~~~~~~~~~~
    A brief description goes here.
    :copyright: (c) 2022 by isanghyeon.

    The MIT License
    Copyright (c) 2022 isanghyeon all rights reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from flask import g
from flask_restx import Resource, fields, Namespace, model
import sys, os, json, datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .customResponse import CustomizeResponse
from .customField import StringToJSON

from model.message import message as messageDBSchema
from model.chatroom import chatroom as chatroomDBSchema

ns = Namespace('api/chat/msg', description='msg information operator')

msgNSBaseModel = ns.model(
    "msg api model",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "UserUniqKey": fields.String(required=True, description=""),
        "ChatUniqKey": fields.String(required=True, description=""),
        "UserName": fields.String(required=True, description=""),
        "MessageType": fields.Boolean(required=False, description=""),
        "MessageData": fields.String(required=False, description=""),
        "MediaDataPath": fields.String(required=False, description=""),
        "MessageTimestamp": fields.DateTime(readonly=True, description="")
    }
)

responseModel = ns.model(
    "response api model",
    {
        "status": fields.String(readonly=True, description=""),
        "message": fields.String(readonly=True, description=""),
        "data": StringToJSON(readonly=True, description="")
    }
)


class msgDAO(object):
    def __init__(self):
        self.selectData = None
        self.insertData = None

    @staticmethod
    def ErrorHandler():
        return {
                   "status": 404,
                   "message": "Chatting Room Not Found",
                   "data": [{
                       "UserUniqKey": "",
                       "ChatUniqKey": "",
                       "UserName": "",
                       "MessageType": "",
                       "MessageData": "",
                       "MediaDataPath": "",
                       "MessageTimestamp": ""
                   }, ]
               }, 404

    @staticmethod
    def CheckChattingRoomWithKey(key=None) -> bool:
        if key is None:
            return False

        return True if g.MsgDB.query(chatroomDBSchema).filter(chatroomDBSchema.ChatUniqKey == key).count() == 1 else False

    def MessageGetAllData(self, key: str):
        self.selectData = g.MsgDB.query(messageDBSchema).filter(messageDBSchema.ChatUniqKey == key).all() if self.CheckChattingRoomWithKey(key) is True else []

        if not self.selectData:
            return self.ErrorHandler()

        ResultObject = {
            "status": 200,
            "message": "success",
            "data": []
        }

        for idx in range(len(self.selectData)):
            ResultObject["data"].append({
                "UserUniqKey": f"{self.selectData[idx].UserUniqKey}",
                "ChatUniqKey": f"{self.selectData[idx].ChatUniqKey}",
                "UserName": f"{self.selectData[idx].UserName}",
                "MessageType": f"{self.selectData[idx].MessageType}",
                "MessageData": f"{self.selectData[idx].MessageData}",
                "MediaDataPath": f"{self.selectData[idx].MediaDataPath}",
                "MessageTimestamp": f"{self.selectData[idx].MessageTimestamp}"
            })

        return ResultObject

    def MessageGetUserData(self, key_chat: str, key_user: str):
        self.selectData = g.MsgDB.query(messageDBSchema).filter(messageDBSchema.ChatUniqKey == key_chat,
                                                                messageDBSchema.UserUniqKey == key_user).all() if self.CheckChattingRoomWithKey(key_chat) is True else []

        if not self.selectData:
            return self.ErrorHandler()

        ResultObject = {
            "status": 200,
            "message": "success",
            "data": []
        }

        for idx in range(len(self.selectData)):
            ResultObject["data"].append({
                "UserUniqKey": f"{self.selectData[idx].UserUniqKey}",
                "ChatUniqKey": f"{self.selectData[idx].ChatUniqKey}",
                "UserName": f"{self.selectData[idx].UserName}",
                "MessageType": f"{self.selectData[idx].MessageType}",
                "MessageData": f"{self.selectData[idx].MessageData}",
                "MediaDataPath": f"{self.selectData[idx].MediaDataPath}",
                "MessageTimestamp": f"{self.selectData[idx].MessageTimestamp}"
            })

        return ResultObject

    def MessageCreate(self, data: dict):
        self.insertData = {} if self.CheckChattingRoomWithKey(key=data["ChatUniqKey"]) is False else data

        if not self.insertData:
            self.ErrorHandler()

        try:
            g.MsgDB.add(
                messageDBSchema(
                    UserUniqKey=self.insertData["UserUniqKey"],
                    ChatUniqKey=self.insertData["ChatUniqKey"],
                    UserName=self.insertData["UserName"],
                    MessageType=self.insertData["MessageType"],
                    MessageData=self.insertData["MessageData"],
                    MediaDataPath=self.insertData["MediaDataPath"],
                    MessageTimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )
            g.MsgDB.commit()

            return {
                       "status": 201,
                       "message": "success",
                       "data": [{
                           "UserUniqKey": "",
                           "ChatUniqKey": "",
                           "UserName": "",
                           "MessageType": "",
                           "MessageData": "",
                           "MediaDataPath": "",
                           "MessageTimestamp": ""
                       }, ]
                   }, 201

        except:
            g.MsgDB.rollback()

        return {
                   "status": 400,
                   "message": "failed",
                   "data": [{
                       "UserUniqKey": f"{e}",
                       "ChatUniqKey": "",
                       "UserName": "",
                       "MessageType": "",
                       "MessageData": "",
                       "MediaDataPath": "",
                       "MessageTimestamp": ""
                   }, ]
               }, 400


DAOForMessage = msgDAO()


@ns.route('')
class messageCreate(Resource):
    """Add New Message"""

    @ns.doc('ADD NEW MSG')
    @ns.expect(msgNSBaseModel)
    @ns.marshal_with(responseModel)
    def post(self):
        """Create New msg"""
        return DAOForMessage.MessageCreate(data=ns.payload)


@ns.route('/<string:key_chat>')
@ns.param('key_chat', 'chat id for unique identifier')
class messageAllInformation(Resource):
    """Show All Messages"""

    @ns.doc('GET ALL MESSAGE IN CHATROOM')
    @ns.marshal_with(responseModel)
    def get(self, key_chat):
        """Fetch a given resource"""
        return DAOForMessage.MessageGetAllData(key=key_chat)


@ns.route('/<string:key_chat>/<string:key_user>')
# @ns.response(404, 'not found')
@ns.param('key_chat', 'chat id for unique identifier')
@ns.param('key_user', 'user id for unique identifier')
class messageUserInformation(Resource):
    """Show a User Messages"""

    @ns.doc('GET USER MESSAGE IN CHATROOM')
    @ns.marshal_with(responseModel)
    def get(self, key_chat, key_user):
        """Fetch a given resource"""
        return DAOForMessage.MessageGetUserData(key_chat=key_chat, key_user=key_user)
