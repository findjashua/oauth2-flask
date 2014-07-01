from flask import Flask, request, redirect, session, url_for
import requests
import json
import oauth2
from keys import keys
from configs import scopes
from urls import urls

app = Flask(__name__)
app.secret_key = 'session_secret'

def get_redirect_uri(app_name):
    return 'http://localhost:5000/authorized/{}'.format(app_name)

@app.route('/login/<app_name>')
def login(app_name):
    auth_url = oauth2.get_auth_url(app_name, keys[app_name], scopes[app_name], get_redirect_uri(app_name))
    return redirect(auth_url)

@app.route('/authorized/<app_name>')
def authorized(app_name):
    [err, token] = oauth2.get_err_and_token(request.args, app_name, keys[app_name], get_redirect_uri(app_name))
    if (err != None):
        return err
    session[app_name] = token
    return redirect('/profile/{}'.format(app_name))

@app.route('/profile/<app_name>')
def profile(app_name):
    profile_url = oauth2.get_app_urls(app_name)['profile_url']
    api_req_params = oauth2.get_api_req_params(urls[app_name], keys[app_name], session[app_name])
    response = requests.get(profile_url, params=api_req_params)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
