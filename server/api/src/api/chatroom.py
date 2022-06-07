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
import sys, os, json, datetime, hashlib, time, random
from sqlalchemy import func

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .customResponse import CustomizeResponse
from .customField import StringToJSON
from model.chatroom import chatroom as chatroomDBSchema
from model.user import user as userDBSchema

ns = Namespace('api/chat/room', description='Chat information operator')

chatNSBaseModel = ns.model(
    "chat api model",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        # "ChatUniqKey": fields.String(required=True, description=""),
        "ParticipantUserName": fields.String(required=True, description=""),
        "ParticipantUserUniqKey": fields.String(required=True, description="")
        # "ParticipantNewUserTimestamp": fields.DateTime(required=True, description=""),
        # "LastChatTimestamp": fields.DateTime(required=True, description=""),
        # "CreateTimestamp": fields.DateTime(required=True, description="")
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


class chatDAO(object):
    def __init__(self):
        self.selectData = None
        self.insertData = None
        self.updateData = None
        self.deleteData = None

    @staticmethod
    def ErrorHandler():
        return {
                   "status": 404,
                   "message": "Chat Room Not Found",
                   "data": {
                       "ChatUniqKey": "",
                       "ChatName": "",
                       "ParticipantUserName": "",
                       "ParticipantUserUniqKey": "",
                       "ParticipantNewUserTimestamp": "",
                       "LastChatTimestamp": "",
                       "CreateTimestamp": ""
                   }
               }, 404

    @staticmethod
    def CheckChatRoomWithKey(key=None) -> bool:
        if key is None:
            return False

        return True if g.ChatDB.query(chatroomDBSchema).filter(chatroomDBSchema.ChatUniqKey == key).count() == 1 else False

    @staticmethod
    def CheckUserWithKeyOrUName(key=None, uname=None) -> bool:
        if key is None:
            return True if g.UserDB.query(userDBSchema).filter(userDBSchema.UserName == uname).count() == 1 else False

        if uname is None:
            return True if g.UserDB.query(userDBSchema).filter(userDBSchema.UserUniqKey == key).count() == 1 else False

    def ChatRoomAddUser(self, key_chat: str, data: dict):
        self.updateData = data if (self.CheckUserWithKeyOrUName(key=None, uname=data["ParticipantUserName"]) is True and
                                   self.CheckUserWithKeyOrUName(key=data["ParticipantUserUniqKey"], uname=None) is True) and (self.CheckChatRoomWithKey(key_chat) is True) else []

        if not self.updateData:  # empty list checking
            return self.ErrorHandler()

        def originalData(Type: bool, key_chat: str) -> str:
            return (g.ChatDB.query(chatroomDBSchema.ParticipantUserName).filter(chatroomDBSchema.ChatUniqKey == key_chat).first()).ParticipantUserName if Type is True \
                else (g.ChatDB.query(chatroomDBSchema.ParticipantUserUniqKey).filter(chatroomDBSchema.ChatUniqKey == key_chat).first()).ParticipantUserUniqKey

        try:
            g.ChatDB.query(chatroomDBSchema).filter(chatroomDBSchema.ChatUniqKey == key_chat).update(
                {
                    "ParticipantUserName": func.concat(originalData(Type=True, key_chat=key_chat), ", ", self.updateData["ParticipantUserName"]),
                    "ParticipantUserUniqKey": func.concat(originalData(Type=False, key_chat=key_chat), ", ", self.updateData["ParticipantUserUniqKey"]),
                    "ParticipantNewUserTimestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )

            g.ChatDB.commit()

            return {
                       "status": 200,
                       "message": "success",
                       "data": {
                           "ChatUniqKey": "",
                           "ChatName": "",
                           "ParticipantUserName": "",
                           "ParticipantUserUniqKey": "",
                           "ParticipantNewUserTimestamp": "",
                           "LastChatTimestamp": "",
                           "CreateTimestamp": ""
                       }
                   }, 200

        except:
            g.ChatDB.rollback()

        return {
                   "status": 400,
                   "message": "failed",
                   "data": {
                       "ChatUniqKey": "",
                       "ChatName": "",
                       "ParticipantUserName": "",
                       "ParticipantUserUniqKey": "",
                       "ParticipantNewUserTimestamp": "",
                       "LastChatTimestamp": "",
                       "CreateTimestamp": ""
                   }
               }, 400

    def ChatRoomGetAllInformation(self):
        self.selectData = g.ChatDB.query(chatroomDBSchema).all()

        if not self.selectData:
            return self.ErrorHandler()

        ResultObject = {
            "status": 200,
            "message": "success",
            "data": []
        }

        for idx in range(len(self.selectData)):
            ResultObject["data"].append({
                "ChatUniqKey": f"{self.selectData[idx].ChatUniqKey}",
                "ChatName": f"{self.selectData[idx].ChatName}",
                "ParticipantUserName": f"{self.selectData[idx].ParticipantUserName}",
                "ParticipantUserUniqKey": f"{self.selectData[idx].ParticipantUserUniqKey}",
                "ParticipantNewUserTimestamp": f"{self.selectData[idx].ParticipantNewUserTimestamp}",
                "LastChatTimestamp": f"{self.selectData[idx].LastChatTimestamp}",
                "CreateTimestamp": f"{self.selectData[idx].CreateTimestamp}"
            })

        return ResultObject

    def ChatRoomGetUserInformation(self, key_user: str, uname: str):
        self.selectData = g.ChatDB.query(chatroomDBSchema).filter(chatroomDBSchema.ParticipantUserUniqKey.like("%" + key_user + "%"),
                                                                  chatroomDBSchema.ParticipantUserName.like("%" + uname + "%")).all()

        if not self.selectData:
            return self.ErrorHandler()

        ResultObject = {
            "status": 200,
            "message": "success",
            "data": []
        }

        for idx in range(len(self.selectData)):
            ResultObject["data"].append({
                "ChatUniqKey": f"{self.selectData[idx].ChatUniqKey}",
                "ChatName": f"{self.selectData[idx].ChatName}",
                "ParticipantUserName": f"{self.selectData[idx].ParticipantUserName}",
                "ParticipantUserUniqKey": f"{self.selectData[idx].ParticipantUserUniqKey}",
                "ParticipantNewUserTimestamp": f"{self.selectData[idx].ParticipantNewUserTimestamp}",
                "LastChatTimestamp": f"{self.selectData[idx].LastChatTimestamp}",
                "CreateTimestamp": f"{self.selectData[idx].CreateTimestamp}"
            })

        return ResultObject

    def ChatRoomGetChatInformation(self, key_chat: str):
        self.selectData = g.ChatDB.query(chatroomDBSchema).filter(chatroomDBSchema.ChatUniqKey == key_chat).first()

        if not self.selectData:
            return self.ErrorHandler()

        ResultObject = {
            "status": 200,
            "message": "success",
            "data": {
                "ChatUniqKey": f"{self.selectData.ChatUniqKey}",
                "ChatName": f"{self.selectData.ChatName}",
                "ParticipantUserName": f"{self.selectData.ParticipantUserName}",
                "ParticipantUserUniqKey": f"{self.selectData.ParticipantUserUniqKey}",
                "ParticipantNewUserTimestamp": f"{self.selectData.ParticipantNewUserTimestamp}",
                "LastChatTimestamp": f"{self.selectData.LastChatTimestamp}",
                "CreateTimestamp": f"{self.selectData.CreateTimestamp}"
            }
        }

        return ResultObject

    def ChatRoomCreate(self, data: dict):
        self.insertData = data if self.CheckUserWithKeyOrUName(key=None, uname=data["ParticipantUserName"]) is True \
                                  and self.CheckUserWithKeyOrUName(key=data["ParticipantUserUniqKey"], uname=None) is True else []

        if not self.insertData:  # empty list checking
            return self.ErrorHandler()

        try:
            g.ChatDB.add(
                chatroomDBSchema(
                    ChatUniqKey=hashlib.sha256((str(time.time()) + "-" + self.insertData["ParticipantUserUniqKey"]).encode()).hexdigest(),
                    ChatName=f'{self.insertData["ParticipantUserName"]}' + "\'s " + f"{str(random.randint(1111111, 9999999))}th" + " chat room",
                    ParticipantUserName=self.insertData["ParticipantUserName"],
                    ParticipantUserUniqKey=self.insertData["ParticipantUserUniqKey"],
                    ParticipantNewUserTimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    LastChatTimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    CreateTimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )
            g.ChatDB.commit()

            return {
                       "status": 201,
                       "message": "success",
                       "data": {
                           "ChatUniqKey": "",
                           "ChatName": "",
                           "ParticipantUserName": "",
                           "ParticipantUserUniqKey": "",
                           "ParticipantNewUserTimestamp": "",
                           "LastChatTimestamp": "",
                           "CreateTimestamp": ""
                       }
                   }, 201

        except:
            g.ChatDB.rollback()

        return {
                   "status": 400,
                   "message": "failed",
                   "data": {
                       "ChatUniqKey": "",
                       "ChatName": "",
                       "ParticipantUserName": "",
                       "ParticipantUserUniqKey": "",
                       "ParticipantNewUserTimestamp": "",
                       "LastChatTimestamp": "",
                       "CreateTimestamp": ""
                   }
               }, 400


DAOForChatroom = chatDAO()


@ns.route('')
class ChatRoom(Resource):
    """Get All Chat Rooms or Add Chat Room"""

    @ns.doc('GET ALL CHATROOM')
    @ns.marshal_with(responseModel)
    def get(self):
        """Fetch a given resource"""
        return DAOForChatroom.ChatRoomGetAllInformation()

    @ns.doc('ADD NEW MSG')
    @ns.expect(chatNSBaseModel)
    @ns.marshal_with(responseModel)
    def post(self):
        """Create New chat"""
        return DAOForChatroom.ChatRoomCreate(data=ns.payload)


@ns.route('/<string:key_user>/<string:uname>')
# @ns.response(404, 'not found')
@ns.param('key_user', 'user id for unique identifier')
@ns.param('uname', 'user name for unique identifier')
class ChatRoomInformation(Resource):
    """Show include user all chat item """

    @ns.doc('GET INCLUDING USER CHATROOM')
    @ns.marshal_with(responseModel)
    def get(self, key_user, uname):
        """Fetch a given resource"""
        return DAOForChatroom.ChatRoomGetUserInformation(key_user=key_user, uname=uname)


@ns.route('<string:key_chat>')
@ns.param('key_chat', 'chat key for unique identifier')
class ChatRoomAllInformation(Resource):
    """Show a chat item"""

    @ns.doc('GET CHATROOM')
    @ns.marshal_with(responseModel)
    def get(self, key_chat):
        """Fetch a given resource"""
        return DAOForChatroom.ChatRoomGetChatInformation(key_chat=key_chat)

    @ns.doc('UPDATE USER')
    @ns.expect(chatNSBaseModel)
    @ns.marshal_with(responseModel)
    def patch(self, key_chat):
        """UPDATE USER"""
        return DAOForChatroom.ChatRoomAddUser(key_chat=key_chat, data=ns.payload)
