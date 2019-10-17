# SR.se restapi Wrapper
#### Description
Wrapper around SR API for learning purposes

#### Dependencies:
pip install requests

#### Simple usage:

Example will show previous song played on SR P3

    import srapi

    data = srapi.SrData("http://api.sr.se/api/v2/playlists/rightnow?channelid=2576&format=json")

    data.songInfo()



#### Todo:

1. Adding support for SR VMA (Important message for society)
2. Add support for music top lists
3. Get current playing song