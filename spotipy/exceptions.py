class SpotifyException(Exception):
    def __init__(self, http_status_code, code, msg, headers=None):
        self.http_status_code = http_status_code
        self.code = code
        self.msg = msg
        # `headers` is used to support `Retry-After` in the event of a
        # 429 status code.
        if headers is None:
            headers = {}
        self.headers = headers

    def __str__(self):
        return f'''
        HTTP Status Code: {self.http_status_code}
        Code: {self.code}
        {self.msg}'''


class SpotifyCredentialsException(Exception):
    def __str__(self):
        return '''
        You need to set your Spotify API credentials. You can do this by
        setting environment variables like so:

        export SPOTIPY_CLIENT_ID='your-spotify-client-id'
        export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
        export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

        Get your credentials at
            https://developer.spotify.com/my-applications
        '''


class SendGridCredentialsException(Exception):
    def __str__(self):
        return '''
            You need to set your SendGrid API credentials. You can do this by
            setting environment variables like so:

            export SENDGRID_API_KEY='your-sendgrid-api-key'
            export SENDGRID_SENDER='your-sendgrid-sender-email'
        '''
