import urllib.request
import urllib.error
import urllib.parse
from urllib.parse import urlencode
import re


def search(query):
    query = query.replace(' ', '+')

    res = urllib.request.urlopen(
        'https://www.youtube.com/results?search_query=' + urlencode({'search_query': query}))

    html = res.read().decode('utf-8')

    keys = re.findall(r'watch\?v=(.{11})', html)

    return keys[0]
