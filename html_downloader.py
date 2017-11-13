#coding:utf8
import urllib.request
import ssl

class HtmlDownLoader(object):
    def download(self,url):
        if url is None:
            return None
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)

        if response.getcode() != 200:
            return None

        return response.read()
