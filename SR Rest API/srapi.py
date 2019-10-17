"""
Todo: implement VMA
Todo vma = "http://api.sr.se/api/v2/vma?format=json"
DONE music = "http://api.sr.se/api/v2/playlists/rightnow?channelid=2576&format=json"
"""

import requests


class SrData:
    def __init__(self,api_url):
        '''Insert SR api URL example: http://api.sr.se/api/v2/playlists/rightnow?channelid=2576&format=json'''
        self.api_url = api_url

    def getData(self):
        '''Get the JSONdata from url ''' 
        return requests.get(url = self.api_url).json()

    def trackInfo(self):
        '''Get songinfo from previous song in SR playlist API'''
        data = requests.get(url = self.api_url).json()
        artist = data['playlist']['previoussong']['artist']
        title = data['playlist']['previoussong']['title']
        composer = data['playlist']['previoussong']['composer']
        recordLabel = data['playlist']['previoussong']['recordlabel']
        return [artist,title, composer, recordLabel]

    def wasPlaying(self):
        ''''Display artist and title of previous song'''
        playing = print("Förra låten som spelades var %s med %s"%(self.trackInfo()[1], self.trackInfo()[0]))
        return playing

    def songInfo(self):
        '''Get extended song information'''
        info = print(" Artist: %s \n Låt: %s \n Kompositör: %s \n Skivbolag: %s"%(self.trackInfo()[0],self.trackInfo()[1],self.trackInfo()[2],self.trackInfo()[3]))
        return info


