# -*- encoding: UTF-8 -*-
#
# Form based authentication for CherryPy. Requires the
# Session tool to be loaded.
#
import hashlib
import sqlite3
import urllib
import urllib.parse
from html import escape

import cherrypy

SESSION_KEY = '_cp_username'
db = "conf/biostat.db"


def generic(sql):
    conn, ans = "", ""
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        ans = cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()
        return ans


def check_credentials(usr, pwd):
    auth_data = {u[0]: u[1] for u in generic("select `user`, `pwd` FROM `users`")}
    """Verifies credentials for username and password.
    Returns None on success or a string describing the error on failure"""
    # Adapt to your needs
    # if username in ('joe', 'steve') and password == 'secret':
    if usr in auth_data.keys() and hashlib.md5(pwd.encode('utf-8')).hexdigest() == auth_data[usr]:
        return None
    else:
        return u"Incorrect username or password."

        # An example implementation which uses an ORM could be:
        # u = User.get(username)
        # if u is None:
        #     return u"Username %s is unknown to me." % username
        # if u.password != md5.new(password).hexdigest():
        #     return u"Incorrect password"


def check_auth(*args, **kwargs):
    """A tool that looks in config for 'auth.require'. If found and it
    is not None, a login is required and the entry is evaluated as alist of
    conditions that the user must fulfill"""
    conditions = cherrypy.request.config.get('auth.require', None)
    # format GET params
    get_parmas = urllib.parse.quote(cherrypy.request.request_line.split()[1])
    if conditions is not None:
        username = cherrypy.session.get(SESSION_KEY)
        if username:
            cherrypy.request.login = username
            for condition in conditions:
                # A condition is just a callable that returns true orfalse
                if not condition():
                    # Send old page as from_page parameter
                    raise cherrypy.HTTPRedirect("/auth/login?from_page=%s" % get_parmas)
        else:
            # Send old page as from_page parameter
            raise cherrypy.HTTPRedirect("/auth/login?from_page=%s" % get_parmas)


cherrypy.tools.auth = cherrypy.Tool('before_handler', check_auth)


def require(*conditions):
    """A decorator that appends conditions to the auth.require config
    variable."""

    def decorate(f):
        if not hasattr(f, '_cp_config'):
            f._cp_config = dict()
        if 'auth.require' not in f._cp_config:
            f._cp_config['auth.require'] = []
        f._cp_config['auth.require'].extend(conditions)
        return f

    return decorate


# Conditions are callables that return True
# if the user fulfills the conditions they define, False otherwise
#
# They can access the current username as cherrypy.request.login
#
# Define those at will however suits the application.

def member_of(groupname):
    def check():
        # replace with actual check if <username> is in <groupname>
        return cherrypy.request.login == 'joe' and groupname == 'admin'

    return check


def name_is(reqd_username):
    return lambda: reqd_username == cherrypy.request.login


# These might be handy

def any_of(*conditions):
    """Returns True if any of the conditions match"""

    def check():
        for c in conditions:
            if c():
                return True
        return False

    return check


# By default all conditions are required, but this might still be
# needed if you want to use it inside of an any_of(...) condition
def all_of(*conditions):
    """Returns True if all of the conditions match"""

    def check():
        for c in conditions:
            if not c():
                return False
        return True

    return check


# Controller to provide login and logout actions

class AuthController(object):
    def on_login(self, username):
        """Called on successful login"""

    def on_logout(self, username):
        """Called on logout"""

    @staticmethod
    def get_loginform(username, msg="Enter login information", from_page="/"):
        username = escape(username, True)
        from_page = escape(from_page, True)
        return u"""<!DOCTYPE html><html><head> <meta charset="utf-8"> <script src="/public/jquery.min.js"
         type="text/javascript"></script> <script src="/public/material.min.js" type="text/javascript"></script>
         <script src="/public/angular.js" type="text/javascript"></script> <script src="/public/angular-animate.min.js"
         type="text/javascript"></script> <script src="/public/angular-route.min.js" type="text/javascript"></script>
          <script src="/public/angular-aria.min.js" type="text/javascript"></script>
          <script src="/public/angular-messages.min.js"
          type="text/javascript"></script> <script src="/public/angular-material.js" type="text/javascript"></script>
          <script src="/public/ngscrollbar.js" type="text/javascript"></script>
           <script type="text/javascript" src="/public/auth.js">
          </script> <link rel="stylesheet" href="/public/angular-material.min.css" media="screen">
          <link rel="stylesheet" href="/public/app.css" media="screen"><title>Login</title>
          </head><body ng-controller="KanCtrl" ng-app="MyApp" layout="column" layout-align="center center">
          <div class="form-login"> <form method="post" action="/auth/login">
          <input type="hidden" name="from_page" value="{}"/> <div> <md-input-container>
          <label for="form-username">Username</label> <input type="text" name="username"
            id="form-username" autofocus required=""> </md-input-container> &nbsp&nbsp&nbsp&nbsp&nbsp
            <md-input-container> <label for="form-password">Password</label> <input type="password" name="password"
            id="form-password" class="" required="" ng-model=login.pwd> </md-input-container> </div><div layout="row"
            layout-align="space-between center" style="width:100%;"> <div></div><div class="form-actions"> <md-button
             type="submit" class="md-raised md-primary">Sign in</md-button> </div></div></form></div></body>
             </html>""".format(locals()['from_page'])

    @cherrypy.expose
    def login(self, username=None, password=None, from_page="/"):
        if username is None or password is None:
            return self.get_loginform("", from_page=from_page)

        error_msg = check_credentials(username, password)
        if error_msg:
            return self.get_loginform(username, error_msg, from_page)
        else:
            cherrypy.session.regenerate()
            cherrypy.session[SESSION_KEY] = cherrypy.request.login = username
            self.on_login(username)
            raise cherrypy.HTTPRedirect(from_page or "/")

    @cherrypy.expose
    def logout(self, from_page="/"):
        sess = cherrypy.session
        username = sess.get(SESSION_KEY, None)
        sess[SESSION_KEY] = None
        if username:
            cherrypy.request.login = None
            self.on_logout(username)
        raise cherrypy.HTTPRedirect(from_page or "/")

'''
import hashlib
print(hashlib.md5("diegolabammike".encode('utf-8')).hexdigest())
print(hashlib.md5("labam2016".encode('utf-8')).hexdigest())
print(hashlib.md5("user".encode('utf-8')).hexdigest())
'''
