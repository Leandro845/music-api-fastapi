# Import the necessary libraries
from fastapi import FastAPI  # Import FastAPI framework
import musicbrainzngs  # Import MusicBrainzNGS library for music data retrieval
import json  # Import json library for JSON manipulation

# Create a FastAPI instance
app = FastAPI()

# Set user agent for MusicBrainzNGS (optional but recommended)
musicbrainzngs.set_useragent('RockInRollAPI', '1.0', 'example@gmail.com')

# Search band data
@app.get('/{band_name}')
def band_name(band_name: str):
    """
    Endpoint to search for information about a music band.

    Parameters:
    - band_name (str): Name of the band to search for.

    Returns:
    - JSON response containing information about the band.
    """
    band = musicbrainzngs.search_artists(artist=band_name)
    return json.dumps(band, indent=4)

# Search album data
@app.get('/{band_name}/{album}')
def band_album(band_name, album: str):
    """
    Endpoint to search for information about a specific album by a music band.

    Parameters:
    - band_name (str): Name of the band.
    - album (str): Title of the album to search for.

    Returns:
    - JSON response containing information about the album.
    """
    album_ = musicbrainzngs.search_releases(artist=band_name, release=album)
    return json.dumps(album_, indent=4)

# Search song data
@app.get('/{band_name}/{song}')
def band_song(band_name: str, song: str):
    """
    Endpoint to search for information about a specific song by a music band.

    Parameters:
    - band_name (str): Name of the band.
    - song (str): Title of the song to search for.

    Returns:
    - JSON response containing information about the song.
    """
    song_ = musicbrainzngs.search_recordings(artist=band_name, recording=song)
    return json.dumps(song_, indent=4)
