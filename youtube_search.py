import urllib2
import re


def search(query):

    query = query.replace(' ', '+')

    res = urllib2.urlopen(
        'https://www.youtube.com/results?search_query=' + query)
    html = res.read()

    keys = re.findall(r'watch\?v=(.{11})', html)

    return keys[0]
