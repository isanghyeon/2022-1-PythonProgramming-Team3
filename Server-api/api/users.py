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
from model.user import user as userDBSchema

ns = Namespace('api/users', description='User information operator')

userNSBaseModel = ns.model(
    "user api model",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "UserUniqKey": fields.String(required=True, description=""),
        "UserName": fields.String(required=True, description=""),
        "UserAccountID": fields.String(required=True, description=""),
        "UserAccountPW": fields.String(required=True, description=""),
        "LastLoginTimestamp": fields.DateTime(required=True, description=""),
        "CreateTimestamp": fields.DateTime(required=True, description="")
    }
)

userNSUpdateLoginTimeModel = ns.model(
    "user api model update login time",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "LastLoginTimestamp": fields.DateTime(required=True, description="")
    }
)

responseModel = ns.model(
    "response api model",
    {
        "status": fields.String(readonly=True, description=""),
        "message": fields.String(readonly=True, description="")
    }
)


class userDAO(object):
    def __init__(self):
        self.selectData = None
        self.insertData = None
        self.updateData = None

    def get(self, uniqueKey):
        self.selectData = g.MessengerDB.query(userDBSchema).filter(userDBSchema.UserUniqKey == uniqueKey).first()

        if not self.selectData:
            ns.abort(404, f"user doesn't exist")

        return self.selectData

    def create(self, data):
        try:
            self.insertData = data

            g.MessengerDB.add(
                userDBSchema(
                    UserUniqKey=self.insertData["UserUniqKey"],
                    UserName=self.insertData["UserName"],
                    UserAccountID=self.insertData["UserAccountID"],
                    UserAccountPW=self.insertData["UserAccountPW"],
                    LastLoginTimestamp=self.insertData["LastLoginTimestamp"],
                    CreateTimestamp=self.insertData["CreateTimestamp"]
                )
            )
            g.MessengerDB.commit()

            return CustomizeResponse().return_post_http_status_message(Type=True)
        except Exception as e:
            print(e)
            g.MessengerDB.rollback()

        return CustomizeResponse().return_post_http_status_message(Type=False)

    def update(self, data, uniqueKey):
        if not self.get(uniqueKey):
            pass

        try:
            self.updateData = data

            g.MessengerDB.query(userDBSchema).filter(
                userDBSchema.UserUniqKey == uniqueKey
            ).update(
                {'LastLoginTimestamp': self.updateData["LastLoginTimestamp"]}
            )

            g.MessengerDB.commit()

            return CustomizeResponse().return_patch_http_status_message(Type=True)
        except Exception as e:
            g.MessengerDB.rollback()

        return CustomizeResponse().return_patch_http_status_message(Type=False)


DAOForUser = userDAO()


@ns.route('')
class userAdd(Resource):
    """ADD NEW USER"""

    @ns.doc('ADD NEW USER')
    @ns.expect(userNSBaseModel)
    @ns.marshal_with(responseModel)
    def post(self):
        """Create New User"""
        return DAOForUser.create(ns.payload)


@ns.route('/<string:uniqueKey>')
@ns.response(404, 'user not found')
@ns.param('uniqueKey', 'user id for unique identifier')
class userInformation(Resource):
    """Show a single item"""

    @ns.doc('GET USER')
    @ns.marshal_with(userNSBaseModel)
    def get(self, uniqueKey):
        """Fetch a given resource"""
        return DAOForUser.get(uniqueKey=uniqueKey)

    @ns.doc('UPDATE EXIST USER')
    @ns.expect(userNSUpdateLoginTimeModel)
    @ns.marshal_with(responseModel)
    def patch(self, uniqueKey):
        """Update Existing User"""
        return DAOForUser.update(ns.payload, uniqueKey=uniqueKey)
