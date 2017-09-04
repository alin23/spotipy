from setuptools import setup

setup(
    name='spotipy',
    version='2.4.4',
    description='simple client for the Spotify Web API',
    author="@plamere",
    author_email="paul@echonest.com",
    url='http://spotipy.readthedocs.org/',
    install_requires=[
        'requests',
        'six',
        'daiquiri',
        'sendgrid',
        'requests_oauthlib',
        'oauthlib',
    ],
    license='LICENSE.txt',
    packages=['spotipy'])
