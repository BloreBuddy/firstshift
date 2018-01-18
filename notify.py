!/usr/bin/python

import requests

datame = {
  'message': 'Urgent! I need some help.',
  'level': 5,
  'secret': '35926afd4ca93c229ba6201805031273',
  'link': 'http://casualtalk.chatovod.com'
}

resp = requests.post('https://api.pushjet.io/message', data=datame).json()
