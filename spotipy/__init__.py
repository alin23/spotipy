VERSION = '2.0.1'
from .client import Spotify
from .constants import API, Scope, AuthFlow, AudioFeature
from .exceptions import (
    SpotifyException,
    SpotifyCredentialsException,
    SendGridCredentialsException
)
