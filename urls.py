urls = {
    'github': {
        'auth_url': 'https://github.com/login/oauth/authorize',
        'auth_params': {},
        'token_url': 'https://github.com/login/oauth/access_token',
        'token_params': {},
        'api_token_param': 'access_token',
        'profile_url': 'https://api.github.com/user'
    },
    'linkedin': {
        'auth_url': 'https://www.linkedin.com/uas/oauth2/authorization',
        'auth_params': {
            'response_type': 'code'
        },
        'token_url': 'https://www.linkedin.com/uas/oauth2/accessToken',
        'token_params': {
            'grant_type': 'authorization_code'
        },
        'api_token_param': 'access_token'
    },
    'slack': {
        'auth_url': 'https://slack.com/oauth/authorize',
        'auth_params': {},
        'token_url': 'https://slack.com/api/oauth.access',
        'token_params': {},
        'api_token_param': 'token',
        'profile_url': 'https://slack.com/api/auth.test'
    },
    'stackexchange': {
        'auth_url': 'https://stackexchange.com/oauth',
        'auth_params': {},
        'token_url': 'https://stackexchange.com/oauth/access_token',
        'token_params': {},
        'api_token_param': 'access_token',
        'profile_url': 'https://api.stackexchange.com/me?site=stackoverflow'
    }
}
