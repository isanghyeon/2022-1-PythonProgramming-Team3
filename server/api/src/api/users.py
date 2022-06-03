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
from .customField import StringToJSON
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

responseModel = ns.model(
    "response api model",
    {
        "status": fields.String(readonly=True, description=""),
        "message": fields.String(readonly=True, description=""),
        "data": StringToJSON(readonly=True, description="")
    }
)


class userDAO(object):
    def __init__(self):
        self.selectData = None
        self.insertData = None
        self.updateData = None

    @staticmethod
    def ErrorHandler():
        return {
                   "status": 404,
                   "message": "User Not Found",
                   "data": {
                       "UserUniqKey": "",
                       "UserName": ""
                   }
               }, 404

    @staticmethod
    def CheckUserWithKeyOrUName(key=None, uname=None) -> bool:
        if key is None:
            return True if g.UserDB.query(userDBSchema).filter(userDBSchema.UserName == uname).count() == 1 else False

        if uname is None:
            return True if g.UserDB.query(userDBSchema).filter(userDBSchema.UserUniqKey == key).count() == 1 else False

    def UserSignIn(self, uname: str, upw: str):
        self.selectData = g.UserDB.query(userDBSchema).filter(userDBSchema.UserName == uname,
                                                              userDBSchema.UserAccountPW == hashlib.sha256(upw.encode()).hexdigest()).first() if self.CheckUserWithKeyOrUName(
            key=None, uname=uname) is True else []

        if not self.selectData:  # empty list checking
            return self.ErrorHandler()

        try:
            g.UserDB.query(userDBSchema).filter(userDBSchema.UserUniqKey == str(self.selectData.UserUniqKey)).update(
                {"LastLoginTimestamp": f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'}
            )
            g.UserDB.commit()
            return {
                "status": 200,
                "message": "success",
                "data": {
                    "UserUniqKey": self.selectData.UserUniqKey,
                    "UserName": self.selectData.UserName
                }
            }
        except:
            g.UserDB.rollback()

        return {
            "status": 400,
            "message": "failed",
            "data": {
                "UserUniqKey": self.selectData.UserUniqKey,
                "UserName": self.selectData.UserName
            }
        }

    def UserGetInformation(self, key: str):
        self.selectData = g.UserDB.query(userDBSchema).filter(userDBSchema.UserUniqKey == key).first() if self.CheckUserWithKeyOrUName(key=key, uname=None) is True else []

        if not self.selectData:
            return self.ErrorHandler()

        return {
            "status": 200,
            "message": "success",
            "data": {
                "UserUniqKey": self.selectData.UserUniqKey,
                "UserName": self.selectData.UserName
            }
        }

    def UserSinUp(self, data: dict):
        self.insertData = {} if self.CheckUserWithKeyOrUName(key=None, uname=data["UserName"]) is True else data

        if not self.insertData:
            return {
                       "status": 400,
                       "message": "User already exists... ):",
                       "data": {
                           "UserUniqKey": "",
                           "UserName": ""
                       }
                   }, 400

        try:
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

            return {
                       "status": 201,
                       "message": "success",
                       "data": {
                           "UserUniqKey": "",
                           "UserName": ""
                       }
                   }, 201
        except:
            g.UserDB.rollback()

        return {
                   "status": 400,
                   "message": "failed",
                   "data": {
                       "UserUniqKey": "",
                       "UserName": ""
                   }
               }, 400


DAOForUser = userDAO()


@ns.route('')
class userRegister(Resource):
    """ADD NEW USER"""

    @ns.doc('ADD NEW USER')
    @ns.expect(userNSBaseModel)
    @ns.marshal_with(responseModel)
    def post(self):
        """Create New User"""
        return DAOForUser.UserSinUp(data=ns.payload)


@ns.route('/<string:uname>/<string:upw>')
# @ns.response(404, 'Not Found')
@ns.param("uname", "user name")
@ns.param("upw", "user password")
class userLogin(Resource):
    """User validation method"""

    @ns.doc("UESR VALIDATE")
    @ns.marshal_with(responseModel)
    def get(self, uname, upw):
        """Fetch a given resource"""
        return DAOForUser.UserSignIn(uname=uname, upw=upw)


@ns.route('/<string:key_user>')
@ns.param('key_user', 'user id for unique identifier')
class userInformation(Resource):
    """Show and Update a single item information"""

    @ns.doc('GET USER')
    @ns.marshal_with(responseModel)
    def get(self, key_user):
        """Fetch a given resource"""
        return DAOForUser.UserGetInformation(key=key_user)
