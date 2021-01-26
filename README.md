# PLTransfer

A script to transfer your Apple Music/iTunes Library to Spotify

### Requirements:

- iTunes on PC
- Python 3
- Spotify Premium (For API Access)
- A Spotify Developer App

### Getting Started:

First you need an access token, you need to make a Spotify Application on the developer dashboard. Then you need to setup a way to get your OAuth token. Take a look at https://github.com/M4cs/Slack-Spotify-Authentication for an example!

#### YOU NEED TO HAVE THIS SCOPE: `user-library-modify`

Next add the OAuth token you generated to `Line 7` in the `config` dictionary. 

Go to iTunes and select File > Library > Export Library. Save the file as Library.xml in the same folder as the script.

Run `python3 pltransfer.py` and let it work it's magic! **It may take up to 24 hours for all songs to show depending on Spotify's API.**