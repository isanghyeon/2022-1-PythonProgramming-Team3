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
from model.chatroom import chatroom as chatroomDBSchema

ns = Namespace('api/chat/room', description='Chat information operator')

chatNSBaseModel = ns.model(
    "chat api model",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "ChatUniqKey": fields.String(required=True, description=""),
        "ParticipantUName": fields.String(required=True, description=""),
        "ParticipantUniqKey": fields.String(required=True, description=""),
        "NewUserParicipatedTimestamp": fields.DateTime(required=True, description=""),
        "LastChatTimestamp": fields.DateTime(required=True, description=""),
        "CreateTimestamp": fields.DateTime(required=True, description="")
    }
)

chatNSUpdateParticipantUNameModel = ns.model(
    "chat api model update paricipated user name",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "ParticipantUName": fields.String(required=True, description="")
    }
)

chatNSUpdateParticipantUniqKeyModel = ns.model(
    "chat api model update paricipated user unique key",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "ParticipantUniqKey": fields.String(required=True, description="")
    }
)

chatNSUpdateNewUserParicipatedTimeModel = ns.model(
    "chat api model update new user paricipated time",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "NewUserParicipatedTimestamp": fields.DateTime(required=True, description="")
    }
)

chatNSUpdateLastChatTimeModel = ns.model(
    "chat api model update last chat time",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "LastChatTimestamp": fields.DateTime(required=True, description="")
    }
)

chatNSDeleteChatUniqKeyModel = ns.model(
    "chat api model delete chat room",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "ChatUniqKey": fields.String(required=True, description="")
    }
)

responseModel = ns.model(
    "response api model",
    {
        "status": fields.String(readonly=True, description=""),
        "message": fields.String(readonly=True, description="")
    }
)


class chatDAO(object):
    def __init__(self):
        self.selectData = None
        self.insertData = None
        self.updateData = None
        self.deleteData = None

    def get(self, chat_key, user_key):
        self.selectData = g.ChatDB.query(chatroomDBSchema).filter(chatroomDBSchema.ParticipantUniqKey.like(user_key), chatroomDBSchema.ChatUniqKey == chat_key).all()

        if not self.selectData:
            ns.abort(404, f"data doesn't exist")

        return self.selectData

    def create(self, data):
        try:
            self.insertData = data

            g.ChatDB.add(
                chatroomDBSchema(
                    ChatUniqKey=self.insertData["ChatUniqKey"],
                    ParticipantUName=self.insertData["ParticipantUName"],
                    ParticipantUniqKey=self.insertData["ParticipantUniqKey"],
                    NewUserParicipatedTimestamp=self.insertData["NewUserParicipatedTimestamp"],
                    LastChatTimestamp=self.insertData["LastChatTimestamp"],
                    CreateTimestamp=self.insertData["CreateTimestamp"]
                )
            )
            print(self.insertData)
            g.ChatDB.commit()

            return CustomizeResponse().return_post_http_status_message(Type=True)
        except Exception as e:
            g.ChatDB.rollback()

        return CustomizeResponse().return_post_http_status_message(Type=False)

    def update(self, data, chat_key, user_key, type):
        if not self.get(chat_key, user_key) or type not in [1, 2, 3, 4]:
            return CustomizeResponse().return_patch_http_status_message(Type=False)

        if type == 1:
            try:
                self.updateData = data

                g.ChatDB.query(chatroomDBSchema).filter(
                    chatroomDBSchema.ChatUniqKey == chat_key
                ).update(
                    {'ParticipantUName': self.updateData["ParticipantUName"]}
                )

                g.ChatDB.commit()

                return CustomizeResponse().return_patch_http_status_message(Type=True)
            except Exception as e:
                g.ChatDB.rollback()

        if type == 2:
            try:
                self.updateData = data

                g.ChatDB.query(chatroomDBSchema).filter(
                    chatroomDBSchema.ChatUniqKey == chat_key
                ).update(
                    {'ParticipantUniqKey': self.updateData["ParticipantUniqKey"]}
                )

                g.ChatDB.commit()

                return CustomizeResponse().return_patch_http_status_message(Type=True)
            except Exception as e:
                g.ChatDB.rollback()

        if type == 3:
            try:
                self.updateData = data

                g.ChatDB.query(chatroomDBSchema).filter(
                    chatroomDBSchema.ChatUniqKey == chat_key
                ).update(
                    {'NewUserParicipatedTimestamp': self.updateData["NewUserParicipatedTimestamp"]}
                )

                g.ChatDB.commit()

                return CustomizeResponse().return_patch_http_status_message(Type=True)
            except Exception as e:
                g.ChatDB.rollback()

        if type == 4:
            try:
                self.updateData = data

                g.ChatDB.query(chatroomDBSchema).filter(
                    chatroomDBSchema.ChatUniqKey == chat_key
                ).update(
                    {'LastChatTimestamp': self.updateData["LastChatTimestamp"]}
                )

                g.ChatDB.commit()

                return CustomizeResponse().return_patch_http_status_message(Type=True)
            except Exception as e:
                g.ChatDB.rollback()

        return CustomizeResponse().return_patch_http_status_message(Type=False)

    def delete(self, data):
        try:
            self.deleteData = data

            g.ChatDB.query(chatroomDBSchema).filter(
                chatroomDBSchema.ChatUniqKey == self.deleteData["ChatUniqKey"]
            ).delete()

            g.ChatDB.commit()

            return CustomizeResponse().return_delete_http_status_message(Type=True)
        except Exception as e:
            g.ChatDB.rollback()

        return CustomizeResponse().return_delete_http_status_message(Type=False)


DAOForChatroom = chatDAO()


@ns.route('')
class chatAdd(Resource):
    """ADD NEW chat"""

    @ns.doc('ADD NEW MSG')
    @ns.expect(chatNSBaseModel)
    @ns.marshal_with(responseModel)
    def post(self):
        """Create New chat"""
        return DAOForChatroom.create(ns.payload)

    @ns.doc('DELETE EXIST CHATROOM')
    @ns.expect(chatNSDeleteChatUniqKeyModel)
    @ns.marshal_with(responseModel)
    def delete(self):
        """Delete Existing Chat"""
        return DAOForChatroom.delete(ns.payload)


@ns.route('/<string:chat_uniqueKey>/<string:user_uniqueKey>')
@ns.response(404, 'not found')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class chatGet(Resource):
    """Show a chat item"""

    @ns.doc('GET CHATROOM')
    @ns.marshal_list_with(chatNSBaseModel)
    def get(self, chat_uniqueKey, user_uniqueKey):
        """Fetch a given resource"""
        return DAOForChatroom.get(chat_key=chat_uniqueKey, user_key=user_uniqueKey)


@ns.route('/ParticipantUName/<string:chat_uniqueKey>/<string:user_uniqueKey>')
@ns.response(404, 'not found')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class chatPatchParticipantUName(Resource):
    """Update Chat item ParticipantUName"""

    @ns.doc('UPDATE EXIST CHATROOM')
    @ns.expect(chatNSUpdateParticipantUNameModel)  # type 1
    @ns.marshal_with(responseModel)
    def patch(self, chat_uniqueKey, user_uniqueKey):
        """Update ParticipantUName"""
        return DAOForChatroom.update(ns.payload, chat_key=chat_uniqueKey, user_key=user_uniqueKey, type=1)


@ns.route('/ParticipantUniqKey/<string:chat_uniqueKey>/<string:user_uniqueKey>')
@ns.response(404, 'not found')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class chatPatchParticipantUniqKey(Resource):
    """Update Chat item ParticipantUniqKey"""

    @ns.expect(chatNSUpdateParticipantUniqKeyModel)  # type 2
    @ns.marshal_with(responseModel)
    def patch(self, chat_uniqueKey, user_uniqueKey):
        """Update ParticipantUniqKey"""
        return DAOForChatroom.update(ns.payload, chat_key=chat_uniqueKey, user_key=user_uniqueKey, type=2)


@ns.route('/NewUserParicipatedTimestamp/<string:chat_uniqueKey>/<string:user_uniqueKey>')
@ns.response(404, 'not found')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class chatPatchNewUserParicipatedTimestamp(Resource):
    """Update Chat item NewUserParicipatedTimestamp"""

    @ns.expect(chatNSUpdateNewUserParicipatedTimeModel)  # type 3
    @ns.marshal_with(responseModel)
    def patch(self, chat_uniqueKey, user_uniqueKey):
        """Update NewUserParicipatedTimestamp"""
        return DAOForChatroom.update(ns.payload, chat_key=chat_uniqueKey, user_key=user_uniqueKey, type=3)


@ns.route('/LastChatTimestamp/<string:chat_uniqueKey>/<string:user_uniqueKey>')
@ns.response(404, 'not found')
@ns.param('chat_uniqueKey', 'chat id for unique identifier')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class chatPatchLastChatTimestamp(Resource):
    """Update Chat item LastChatTimestamp"""

    @ns.expect(chatNSUpdateLastChatTimeModel)  # type 4
    @ns.marshal_with(responseModel)
    def patch(self, chat_uniqueKey, user_uniqueKey):
        """Update LastChatTimestamp"""
        return DAOForChatroom.update(ns.payload, chat_key=chat_uniqueKey, user_key=user_uniqueKey, type=4)
