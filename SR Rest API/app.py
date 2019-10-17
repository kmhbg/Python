import srapi

data = srapi.SrData("http://api.sr.se/api/v2/playlists/rightnow?channelid=2576&format=json")

data.songInfo()

srapi.