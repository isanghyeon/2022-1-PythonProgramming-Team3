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
        "message": fields.String(readonly=True, description="")
    }
)


class msgDAO(object):
    def __init__(self):
        self.selectData = None
        self.insertData = None

    def ChatRoomValidator(self, key_chat: str):
        self.selectData = g.ChatDB.query(chatroomDBSchema).filter(chatroomDBSchema.ChatUniqKey == key_chat).count()

        if self.selectData < 1:
            ns.abort(404, f"Chatting Room is not exist")

        return True if self.selectData == 1 else False

    def GetAllMessages(self, key_chat: str):
        if self.ChatRoomValidator(key_chat):
            pass

        self.selectData = g.MsgDB.query(messageDBSchema).filter(messageDBSchema.ChatUniqKey == key_chat).all()

        if not self.selectData:
            ns.abort(404, f"data doesn't exist")

        return self.selectData

    def GetUserMessages(self, key_chat: str, key_user: str):
        if self.ChatRoomValidator(key_chat):
            pass

        self.selectData = g.MsgDB.query(messageDBSchema).filter(messageDBSchema.ChatUniqKey == key_chat, messageDBSchema.UserUniqKey == key_user).all()

        if not self.selectData:
            ns.abort(404, f"data doesn't exist")

        return self.selectData

    def create(self, key_chat: str, data: dict):
        if not self.ChatRoomValidator(key_chat):
            return CustomizeResponse().return_post_http_status_message(Type=False)

        try:
            self.insertData = data
            print(self.insertData)

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
            print(1)
            g.MsgDB.commit()

            return CustomizeResponse().return_post_http_status_message(Type=True)
        except Exception as e:
            print(e)
            g.MsgDB.rollback()

        return CustomizeResponse().return_post_http_status_message(Type=False)


DAOForMessage = msgDAO()


@ns.route('/<string:chat_uniqueKey>')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
class msgAdd(Resource):
    """ADD NEW msg"""

    @ns.doc('ADD NEW MSG')
    @ns.expect(msgNSBaseModel)
    @ns.marshal_with(responseModel)
    def post(self, chat_uniqueKey):
        """Create New msg"""
        return DAOForMessage.create(data=ns.payload, key_chat=chat_uniqueKey)

    @ns.doc('GET ALL MESSAGE IN CHATROOM')
    @ns.marshal_list_with(msgNSBaseModel)
    def get(self, chat_uniqueKey):
        """Fetch a given resource"""
        return DAOForMessage.GetAllMessages(key_chat=chat_uniqueKey)


@ns.route('/<string:chat_uniqueKey>/<string:user_uniqueKey>')
@ns.response(404, 'not found')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class msgAllGet(Resource):
    """Show a single item"""

    @ns.doc('GET USER MSG IN CHATROOM')
    @ns.marshal_list_with(msgNSBaseModel)
    def get(self, chat_uniqueKey, user_uniqueKey):
        """Fetch a given resource"""
        return DAOForMessage.GetUserMessages(key_chat=chat_uniqueKey, key_user=user_uniqueKey)
