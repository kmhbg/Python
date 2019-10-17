import requests

vma = "http://api.sr.se/api/v2/vma?format=json"
music = "http://api.sr.se/api/v2/playlists/rightnow?channelid=2576&format=json"


r = requests.get(url = music)
data = r.json()
#print(data)
artist = data['playlist']['previoussong']['artist']
title = data['playlist']['previoussong']['title']

print("Just nu spelas %s med låten %s"%(artist, title))
""" if resp.status_code != 200:
    # If something went wrong
    #raise a ("GET /vma {}".format(resp.status_code))
    print("Something went wrong")
print(resp.json()['playlist'][0]['previoussong']) """


