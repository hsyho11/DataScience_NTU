import oauth2
import requests,time
def prompt_for_user_token(username, scope=None, client_id = None,
        client_secret = None, redirect_uri = 'http://lab.wubinray.com:5000/callback', cache_path = None):

    cache_path = cache_path or ".cache-" + username
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, 
        scope=scope, cache_path=cache_path)

    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        import webbrowser
        webbrowser.open(auth_url,new=1)
        
        code = requests.get('http://lab.wubinray.com:5000/getcode').text
        while code=='aa':
            code = requests.get('http://lab.wubinray.com:5000/getcode').text
            time.sleep(1)
            
        token_info = sp_oauth.get_access_token(code)
        
    return token_info['access_token']