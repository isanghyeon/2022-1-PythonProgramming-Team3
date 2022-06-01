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
import time

from flask import g
from flask_restx import Resource, fields, Namespace, model
import sys, os, json, datetime, hashlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .customResponse import CustomizeResponse
from model.user import user as userDBSchema

ns = Namespace('api/users', description='User information operator')

userNSBaseModel = ns.model(
    "user api model",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "UserName": fields.String(required=True, description=""),
        "UserAccountPW": fields.String(required=True, description="")
    }
)

userNSValidationModel = ns.model(
    "user validation api model", \
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "UserUniqKey": fields.String(required=True, description=""),
        "UserName": fields.String(required=True, description="")
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

    def UserValidator(self, uname: str, upw: str):
        self.selectData = g.UserDB.query(userDBSchema).filter(userDBSchema.UserName == uname, userDBSchema.UserAccountPW == hashlib.sha256(upw.encode()).hexdigest()).first()

        if not self.selectData:
            ns.abort(404, f"user doesn't exist")

        return CustomizeResponse().return_get_http_status_message(Type=True, data=self.selectData.UserUniqKey)

    def GetUserInfo(self, key: str):
        self.selectData = g.UserDB.query(userDBSchema).filter(userDBSchema.UserUniqKey == key).first()

        if not self.selectData:
            ns.abort(404, f"user doesn't exist")

        return self.selectData

    def CreateUser(self, data: dict):
        if self.GetUserInfo(user_uniqueKey):
            return CustomizeResponse().return_post_http_status_message(Type=False)

        try:
            self.insertData = data

            g.UserDB.add(
                userDBSchema(
                    UserUniqKey=hashlib.sha256((str(time.time()) + "-" + self.insertData["UserName"]).encode()).hexdigest(),
                    UserName=self.insertData["UserName"],
                    UserAccountPW=hashlib.sha256((self.insertData["UserAccountPW"]).encode()).hexdigest(),
                    LastLoginTimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    CreateTimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )
            g.UserDB.commit()

            return CustomizeResponse().return_post_http_status_message(Type=True)
        except Exception as e:
            g.UserDB.rollback()

        return CustomizeResponse().return_post_http_status_message(Type=False)

    def update(self, key: str,  data: dict):
        if not self.GetUserInfo(key):
            pass

        try:
            self.updateData = data

            g.UserDB.query(userDBSchema).filter(
                userDBSchema.UserUniqKey == key
            ).update(
                {'LastLoginTimestamp': self.updateData["LastLoginTimestamp"]}
            )

            g.UserDB.commit()

            return CustomizeResponse().return_patch_http_status_message(Type=True)
        except Exception as e:
            g.UserDB.rollback()

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


@ns.route('/<string:uname>/<string:upw>')
@ns.response(404, 'Not Found')
@ns.response(200, 'OK')
@ns.param("uname", "user name")
@ns.param("upw", "uesr password")
class userValidate(Resource):
    """User validation method"""

    @ns.doc("UESR VALIDATE")
    @ns.marshal_with(responseModel)
    def get(self, uname, upw):
        """Fetch a given resource"""
        return DAOForUser.UserValidator(uname=uname, upw=upw)


@ns.route('/<string:user_uniqueKey>')
@ns.response(404, 'Not Found')
@ns.param('user_uniqueKey', 'user id for unique identifier')
class userInformation(Resource):
    """Show and Update a single item information"""

    @ns.doc('GET USER')
    @ns.marshal_with(userNSValidationModel)
    def get(self, user_uniqueKey):
        """Fetch a given resource"""
        return DAOForUser.GetUserInfo(key=user_uniqueKey)

    @ns.doc('UPDATE EXIST USER')
    @ns.expect(userNSUpdateLoginTimeModel)
    @ns.marshal_with(responseModel)
    def patch(self, user_uniqueKey):
        """Update Existing User"""
        return DAOForUser.CreateUser(ns.payload, key=user_uniqueKey)
