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

ns = Namespace('api/users', description='User information operator')

userNSModel = ns.model(
    "user api model",
    {
        "id": fields.Integer(readonly=True, descriptio=""),
        "UserUniqKey": fields.String(required=True, description=""),
        "UserName": fields.String(required=True, description=""),
        "UserAccountID": fields.String(required=True, description=""),
        "UserAccountPW": fields.String(required=True, description=""),
        "LastLoginTimestamp": fields.DateTime(required=True, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "CreateTimestamp": fields.DateTime(required=True, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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


@ns.route('')
class userAdd(Resource):
    """ADD NEW USER"""

    # @ns.doc('List of all ports data')
    # @ns.marshal_list_with(ports)
    # def get(self):
    #     """Shows Ports data"""
    #     return data_access_object_for_ports.get(id=None, Type=False)

    @ns.doc('ADD NEW USER')
    @ns.expect(userNSModel)
    @ns.marshal_with(responseModel)
    def post(self):
        """Create Ports scanning result"""
        return data_access_object_for_ports.create(ns.payload)


@ns.route('/<string:uniqueKey>')
@ns.response(404, 'user not found')
@ns.param('uniqueKey', 'user id for unique identifier')
class userInformation(Resource):
    """Show a single Ports item"""

    @ns.doc('Get single Ports')
    @ns.marshal_list_with(userNSModel)
    def get(self, uniqueKey):
        """Fetch a given resource"""
        return data_access_object_for_ports.get(uniqueKey)