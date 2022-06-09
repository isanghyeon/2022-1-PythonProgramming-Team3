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

from flask import (
    Flask, g
)
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS
from flask_migrate import Migrate, migrate, upgrade, merge
from flask_sqlalchemy import SQLAlchemy
from model import UserDB, MsgDB, ChatDB


def create_app(config=None):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CORS(app, resource={r'/api/*': {"Access-Control-Allow-Origin": "*"}})
    CORS(app, resource={r'/api/*': {"Access-Control-Allow-Credentials": True}})

    # Config initialization
    from config import Developments_config, Production_config
    if app.config['DEBUG']:
        config = Developments_config()
    else:
        config = Production_config()

    app.config.from_object(config)

    # DATABASE API route initialization.
    from api import bp as api
    app.register_blueprint(api)

    # App context initialization
    app.app_context().push()

    # Database initialization
    UserDB.init_app(app)
    UserDB.app = app

    MsgDB.init_app(app)
    MsgDB.app = app

    ChatDB.init_app(app)
    ChatDB.app = app

    @app.before_request
    def before_request():
        # g object session initialization
        g.UserDB = UserDB.session
        g.MsgDB = MsgDB.session
        g.ChatDB = ChatDB.session

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'UserDB'):
            g.UserDB.close()

        if hasattr(g, 'MsgDB'):
            g.MsgDB.close()

        if hasattr(g, 'ChatDB'):
            g.ChatDB.close()

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(host="0.0.0.0", port=80, debug=False)  # 40010
