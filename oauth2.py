import requests
from urls import urls

def get_param_str(param_dict):
    arr = ['&' + key + '=' + val for key, val in param_dict.iteritems()]
    arr = list(('').join(arr))
    arr[0] = '?'
    return ('').join(arr)

def get_state(app_name):
    return app_name + '_state'

def get_app_urls(app_name):
    return urls[app_name]

def get_auth_url(app_name, keys, scope, redirect_uri):
    app_urls = get_app_urls(app_name)
    auth_url = app_urls['auth_url']
    auth_params = app_urls['auth_params']
    auth_params['client_id'] = keys['client_id']
    auth_params['scope'] = scope
    auth_params['state'] = get_state(app_name)
    auth_params['redirect_uri'] = redirect_uri
    return(auth_url+get_param_str(auth_params))

def get_token_params(query, app_urls, keys, redirect_uri):
    token_params = app_urls['token_params']
    token_params['code'] = query.get('code', '')
    token_params['client_id'] = keys['client_id']
    token_params['client_secret'] = keys['client_secret']
    token_params['redirect_uri'] = redirect_uri
    return token_params

def get_err_and_token(query, app_name, keys, redirect_uri):
    error = query.get('error', '')
    if error != '' :
        return [error, None]
    state = query.get('state','')
    if get_state(app_name) != state :
        return ['received incorrect state {}'.format(state), None]
    app_urls = get_app_urls(app_name)
    token_params = get_token_params(query, app_urls, keys, redirect_uri)
    headers = {'accept': 'application/json'}
    response = requests.post(app_urls['token_url'], data=token_params, headers=headers)
    try:
        return [None, response.json()['access_token']]
    except ValueError, e:
        return [None, response.text.split('access_token=')[1].split('&')[0]]

def get_api_req_params(app_urls, app_keys, access_token):
    params = {app_urls['api_token_param']: access_token, 'key': app_keys['request_key']}
    return params
