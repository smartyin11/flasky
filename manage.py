#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'the entry'

__author__ = 'Smart Yin'

import os
from app import create_app, db
from app.models import User, Role
from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('MYFLASKY_CONFIG') or 'default')
manager = Manager(app)
migrage = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, user=User, role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
